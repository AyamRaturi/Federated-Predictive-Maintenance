import flwr as fl

if __name__ == "__main__":
    print("Starting the Central Aggregation Server...")
    # Start the Flower server on port 8080 for 3 rounds of training
    fl.server.start_server(
        server_address="127.0.0.1:8080",
        config=fl.server.ServerConfig(num_rounds=3)
    )