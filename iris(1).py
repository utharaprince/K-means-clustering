# -*- coding: utf-8 -*-
"""iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GGFEKde9dav9s3727c4YqzJAABHY7C7W

# Predict the optimum number of clusters and represent it visually in iris dataset

# DONE BY 
 
#  UTHARA PRINCE

importing required library
"""

import pandas as pd
from sklearn import datasets 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

"""importing the iris dataset """

iris=datasets.load_iris()
Data=pd.DataFrame(iris.data , columns=iris.feature_names)
Data

x=Data.iloc[:,[0,1,2,3]].values
x

"""Using the elbow method to find out the number od clusters required"""

wcs=[]
for i in range(1,11):
  km=KMeans(n_clusters=i,init='k-means++',max_iter=100, random_state=42)
  km.fit(x)
  wcs.append(km.inertia_)
plt.plot(range(1,11),wcs)

"""cluster=3

using the kmeans algorithm to to make 3 clusters
"""

kmean=KMeans(n_clusters=3,init='k-means++',max_iter=100, random_state=42)
  y_means=kmean.fit_predict(x)
  y_means

"""Plotting the clusters with the sepal width and sepal length"""

plt.scatter(x[y_means == 0, 0], x[y_means == 0, 1], s = 100, c = 'red', label = 'Iris-setosa')
plt.scatter(x[y_means == 1, 0], x[y_means == 1, 1], s = 100, c = 'blue', label = 'Iris-versicolour')
plt.scatter(x[y_means == 2, 0], x[y_means == 2, 1], s = 100, c = 'green', label = 'Iris-virginica')

plt.scatter(kmean.cluster_centers_[:,0], kmean.cluster_centers_[:,1], c='black', marker='*',label='Centroid' ,s=250)
plt.legend()

Data['cluster']=y_means
Data[['cluster','sepal width (cm)','sepal length (cm)']]