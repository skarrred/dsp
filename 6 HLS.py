# Practical 6: Build the time hub, links, and satellites

import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
def create_time_hub_graph():
    G = nx.DiGraph()
    
    # Adding nodes
    hubs = ["Hub1", "Hub2"]
    links = ["Link1", "Link2", "Link3"]
    satellites = ["Sat1", "Sat2", "Sat3", "Sat4"]
    
    for node in hubs + links + satellites:
        G.add_node(node)
    
    # Adding edges
    edges = [("Hub1", "Link1"), ("Hub1", "Link2"), ("Hub2", "Link3"),
             ("Link1", "Sat1"), ("Link1", "Sat2"), ("Link2", "Sat3"),
             ("Link3", "Sat4")]
    
    G.add_edges_from(edges)
    
    return G

# Plot the graph
def plot_graph(G):
    plt.figure(figsize=(8,6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

if __name__ == "__main__":
    G = create_time_hub_graph()
    plot_graph(G)
