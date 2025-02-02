# Practical 5h: Using the given data, Write a Python/R program to plan the shipping routes from best-fit international logistics

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Create graph
def create_shipping_graph(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['Source'], row['Destination'], weight=row['Cost'])
    return G

# Find shortest paths
def find_best_routes(G, source):
    return nx.single_source_dijkstra_path(G, source)

if __name__ == "__main__":
    file_path = "shipping_routes.csv"  # Update with actual file
    df = load_data(file_path)
    G = create_shipping_graph(df)
    source = "PortA"  # Update with actual source
    routes = find_best_routes(G, source)
    print("Best Shipping Routes:", routes)
