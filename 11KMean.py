import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("sales_data_sample.csv", encoding='latin')
print(df.head())  # Display first few rows of the dataset

print(df.dtypes)

X = df.iloc[:, [3,4]].values  # Adjust columns to fit your data structure

wcss = []   

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
ks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow Method")
plt.xlabel("K value")
plt.ylabel("WCSS")
plt.show()  # To display the plot

print(df.describe())

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
scaled = ss.fit_transform(X)

wcss = []
for i in range(1, 11):
    clustering = KMeans(n_clusters=i, init="k-means++", random_state=42)
    clustering.fit(scaled)
    wcss.append(clustering.inertia_)
    
plt.plot(ks, wcss, 'bx-')
plt.title("Elbow Method (Scaled Data)")
plt.xlabel("K value")
plt.ylabel("WCSS")
plt.show()