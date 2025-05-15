import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
# Replace with the path to your condo rent data file
data = pd.read_excel('/mnt/data/Condo_Data_PostCode.xlsx')

# Example: Selecting relevant features (adjust column names as per your dataset)
# Assume 'price', 'size', and 'bedrooms' are relevant for clustering
features = data[['price', 'size', 'bedrooms']]

# Standardize the data for better clustering performance
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# K-means Clustering
# Choose the number of clusters (e.g., 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
data['kmeans_cluster'] = kmeans.fit_predict(features_scaled)

# Visualize the K-means Clustering results
sns.scatterplot(x=features_scaled[:, 0], y=features_scaled[:, 1], hue=data['kmeans_cluster'], palette='viridis')
plt.xlabel('Scaled Price')
plt.ylabel('Scaled Size')
plt.title('K-means Clustering of Condo Rentals')
plt.show()

# Hierarchical Clustering
# Using the 'ward' method for linkage, which minimizes variance within clusters
linked = linkage(features_scaled, method='ward')

# Create a dendrogram to visualize hierarchical clustering
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=data.index, distance_sort='descending', show_leaf_counts=True)
plt.title('Dendrogram for Condo Rentals')
plt.xlabel('Condo Index')
plt.ylabel('Euclidean distances')
plt.show()

# Save the segmented data
# This will create a new file with the clustering results
data.to_excel('/mnt/data/Segmented_Condo_Data.xlsx', index=False)
