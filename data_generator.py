import pandas as pd
import numpy as np
import os

def generate_client_data(client_id, num_samples=1000):
    np.random.seed(42 + client_id) 
    temperature = np.random.normal(loc=70, scale=5, size=num_samples)
    vibration = np.random.normal(loc=5, scale=1, size=num_samples)
    
    failure_mask = np.random.rand(num_samples) > 0.90
    temperature[failure_mask] += np.random.normal(20, 5, sum(failure_mask))
    vibration[failure_mask] += np.random.normal(3, 1, sum(failure_mask))
    
    labels = ((temperature > 85) | (vibration > 7.5)).astype(int)
    
    df = pd.DataFrame({'temperature': temperature, 'vibration': vibration, 'failure': labels})
    
    os.makedirs('data', exist_ok=True)
    file_path = f'data/client_{client_id}.csv'
    df.to_csv(file_path, index=False)
    print(f"Generated dataset for Machine {client_id} -> {file_path}")

if __name__ == "__main__":
    for i in range(1, 4):
        generate_client_data(client_id=i, num_samples=1500)
    print("Data generation complete!")