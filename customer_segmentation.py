#/usr/bin/python3.7
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
#!wget -q -o 'customer_segmentation.csv' https://cocl.us/customer_dataset
print('Data downloaded!')
customers_df=pd.read_csv('customer_segmentation.csv')
print(customers_df.head())

df=customers_df.drop('Address', axis=1)
df.head()
from sklearn.preprocessing import StandardScaler
X=df.values[:,1:]
X=np.nan_to_num(X)
print(X)
cluster_dataset=StandardScaler().fit_transform(X)
print(cluster_dataset)
### modeling
num_clusters=3
k_means=KMeans(init="k-means++",n_clusters,n_nit=12)
k_means.fit(cluster_dataset)
labels = k_means.labels_
print(labels)
df["Labels"]=labels
df.head(5)
df.groupby('Labels').mean()
