import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Reading the dataset from CSV file 'buildings.csv'
data = pd.read_csv('buildings.csv')  # Adjust the path as necessary

# Selecting only numerical features for clustering
numerical_features = data[['Year', 'Livable_Space', 'Volume', 'FloorCount', 'RoomCount', 'NonRoomCount', 'BuildingArea']]

# Standardizing the numerical features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(numerical_features)

# Calculating WCSS for different numbers of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(features_scaled)
    wcss.append(kmeans.inertia_)

# Plotting the results of the Elbow Method
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Method to Determine Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.xticks(range(1, 11))
plt.grid(True)
plt.show()
