# Federated Learning for Predictive Maintenance ⚙️🔒

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Flower](https://img.shields.io/badge/Federated_Learning-Flower-FFD21E.svg)

## 📌 The Problem
Industrial machines generate massive sensor data. Sending all this raw data to the cloud is expensive and poses privacy risks.

## 💡 The Solution
This project uses **Federated Learning** to train a model across multiple "factory machines" without the data ever leaving the local device. Only the mathematical updates (weights) are shared with the Central Server.

## 🏗️ Architecture
1. **Central Server (`server.py`):** Coordinates the training and averages the models.
2. **Edge Clients (`client.py`):** Trains the model locally on specific machine sensor data.

## 🚀 How to Run
1. Generate data: `python data_generator.py`
2. Start Server: `python server.py`
3. Start Clients in new terminals: `python client.py 1`, `python client.py 2`, etc.