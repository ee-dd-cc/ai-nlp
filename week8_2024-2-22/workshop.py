from sklearn.cluster import KMeans
import pandas as pd

customer_data = pd.read_csv('./customer.csv')

# Select the features of the cluster
X = customer_data[['Annual Income (k$)', 'Spending Score (1-100)']].values
# print(X)

# select 5 clusters, n_init = auto, max_iter = 300
kmeans = KMeans(n_clusters = 5, random_state = 0, n_init = 'auto', max_iter = 300).fit(X)

# get the cluster centers
cluster_centers = kmeans.cluster_centers_

print('The cluster centers is: \n',cluster_centers)

# Get the labels
labels = kmeans.labels_
print('The labels are:\n', labels)

# Add cluster to csv and make the number start at 1
customer_data['Cluster'] = labels + 1
print('The customer dataset is:\n', customer_data)
