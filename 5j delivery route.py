# Practical 5j: Write a Python program to create delivery route using the given data

import pandas as pd
import networkx as nx

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Create graph and find shortest delivery route
def create_delivery_route(df, source, destination):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['Source'], row['Destination'], weight=row['Distance'])
    shortest_path = nx.shortest_path(G, source=source, target=destination, weight='Distance')
    return shortest_path

if __name__ == "__main__":
    file_path = "delivery_data.csv"  # Update with actual file
    df = load_data(file_path)
    source, destination = "WarehouseA", "CustomerB"  # Update with actual locations
    route = create_delivery_route(df, source, destination)
    print("Optimal Delivery Route:", route)
