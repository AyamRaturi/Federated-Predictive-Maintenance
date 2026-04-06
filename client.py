import flwr as fl
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
import sys
import warnings

warnings.simplefilter('ignore')

try:
    machine_id = sys.argv[1]
except IndexError:
    print("Please provide a Machine ID! Example: python client.py 1")
    sys.exit()

print(f"Machine {machine_id} loading local sensor data...")
df = pd.read_csv(f"data/client_{machine_id}.csv")
X = df[['temperature', 'vibration']].values
y = df['failure'].values

model = LogisticRegression(warm_start=True, max_iter=1)
model.classes_ = np.array([0, 1])
model.coef_ = np.zeros((1, 2))
model.intercept_ = np.zeros((1,))

class FactoryMachine(fl.client.NumPyClient):
    def get_parameters(self, config):
        return [model.coef_, model.intercept_]

    def set_parameters(self, parameters):
        model.coef_ = parameters[0]
        model.intercept_ = parameters[1]

    def fit(self, parameters, config):
        self.set_parameters(parameters)
        model.fit(X, y)
        print(f"Machine {machine_id} finished local training.")
        return self.get_parameters(config={}), len(X), {}

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)
        loss = log_loss(y, model.predict_proba(X))
        accuracy = model.score(X, y)
        return loss, len(X), {"accuracy": accuracy}

if __name__ == "__main__":
    print(f"Connecting Machine {machine_id} to Server...")
    fl.client.start_client(
        server_address="127.0.0.1:8080", 
        client=FactoryMachine().to_client()
    )