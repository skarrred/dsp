# Practical 5c: Write a Python/R program to build an acyclic graph

import networkx as nx
import matplotlib.pyplot as plt

# Create Directed Acyclic Graph (DAG)
def create_acyclic_graph():
    G = nx.DiGraph()
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    G.add_edges_from(edges)
    return G

# Plot the graph
def plot_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='black', arrows=True)
    plt.show()

if __name__ == "__main__":
    G = create_acyclic_graph()
    plot_graph(G)
