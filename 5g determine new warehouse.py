# Practical 5g: Write a Python/R program using data science via clustering to determine new warehouse using the given data

import pandas as pd
from sklearn.cluster import KMeans

# Load data
def load_data(file_path):
    return pd.read_csv(file_path)

# Apply K-Means clustering
def cluster_warehouses(df, num_clusters=3):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    df['Cluster'] = kmeans.fit_predict(df[['Latitude', 'Longitude']])
    return df, kmeans.cluster_centers_

if __name__ == "__main__":
    file_path = "warehouse_cluster_data.csv"  # Update with actual file
    df = load_data(file_path)
    clustered_df, centers = cluster_warehouses(df)
    print("Cluster Centers:", centers)