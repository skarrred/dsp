# Practical 5b: Write a Python/R program to create the network routing diagram from the given data on routers

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Create network graph
def create_network_graph(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['Source'], row['Destination'], weight=row['Cost'])
    return G

# Plot the graph
def plot_network(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

if __name__ == "__main__":
    file_path = "network_data.csv"  # Update with actual file
    df = load_data(file_path)
    G = create_network_graph(df)
    plot_network(G)
