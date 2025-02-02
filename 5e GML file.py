# Practical 5e: Write a Python/R program to generate a GML file from the given CSV file

import networkx as nx
import pandas as pd

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Create graph and export as GML
def generate_gml(df, output_file):
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['Source'], row['Destination'], weight=row['Cost'])
    nx.write_gml(G, output_file)

if __name__ == "__main__":
    file_path = "graph_data.csv"  # Update with actual file
    output_file = "graph_output.gml"
    df = load_data(file_path)
    generate_gml(df, output_file)
    print(f"GML file saved as {output_file}")
