import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# loading the feaute engeenered dataset
rfm=pd.read_csv("data/customer_features.csv")
print("--------------Printing first 5 lines of data----------")
print(rfm.head())


# applying standard scaler for scaling 
scaler = StandardScaler()
rfm_scaled=scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])


# Inertia = Sum of squared distances of each point to its nearest cluster centroid
inertia = []

for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(rfm_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 10), inertia, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.tight_layout()
plt.savefig("plots/elbow_method.png",dpi=300)
plt.close()

# creating a Kmeans object and applying it 
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# For analyzing clusters
print("Look of clusters mean")
print(rfm.groupby('Cluster').mean())


# Function to label clusters for segregation
def label_customer(row):
    if row['Monetary'] > 1000 and row['Frequency'] > 5:
        return "High Value"
    elif row['Frequency'] > 5:
        return "Loyal"
    elif row['Recency'] > 100:
        return "At Risk"
    else:
        return "Low Value"

rfm['Segment'] = rfm.apply(label_customer, axis=1)


sns.scatterplot(
    x=rfm['Recency'],
    y=rfm['Monetary'],
    hue=rfm['Segment']
)
plt.tight_layout()

plt.savefig("plots/customer_segments.png",dpi=300)
plt.close()

rfm.to_csv("data/customer_segments.csv", index=False)

