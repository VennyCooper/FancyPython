'''
README

Requirements:
   - numpy
   - copy
   - matplotlib

Python:
   - 3.x

Inputs:
   - data: list or np.ndarray (represents the collection of points to cluster)
   - k: the number of clusters
   - plot_before: whether to display the raw point distribution figure
   - plot_after: whether to display the point distribution figure with clusters

Usage:
   - TODO
'''

import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt

class K_Means_Clustering():

   def __init__(self, data, k: int):
      self.data = data
      self.k = k
      self.pre_check()
      # data_shape: (data_point_count, point_dimension)
      self.data_shape = self.data.shape
      # cluster_labels: collection of centroid (cluster) index that each data point belongs to
      # it is the assignment: each point to each cluster
      self.cluster_labels = np.zeros(self.data_shape[0])
      # centroids: cluster centers
      self.centroids = np.zeros((k, self.data_shape[1]))


   def pre_check(self):
      # check k: k is integer && k > 0
      if type(self.k) != int or self.k < 0:
         raise Exception('[k] should be a positive integer number')
      # check data: each data element should be float number
      if type(self.data[0][0]) != float:
         print('Warning: Minimum elements in input data are not float numbers. Type conversion will be done automatically.')
         self.data = [[float(x) for x in d] for d in self.data]
      # convert input data: to ndarray
      if type(self.data) != np.ndarray:
         self.data = np.asarray(self.data)
         print('Warning: Input data should be converted to ndarray. Type conversion will be done automatically.')
      for data_item in self.data:
         if type(data_item) != np.ndarray:
            data_item = np.asarray(data_item)
            print('Warning: Elements in input data should be converted to ndarray. Type conversion will be done automatically.')   


   def cal_distance(self, x, y, ax=1):
      return np.linalg.norm(x-y, axis=ax)


   def initialize_centroids(self):
      data_col_size = self.data.shape[1]
      c_init = np.zeros((self.k, data_col_size))
      for col_index in range(data_col_size):
         col_min, col_max = np.min(self.data[:,col_index]), np.max(self.data[:,col_index])
         c_col = (col_max - col_min) * np.random.random_sample(size=self.k) + col_min
         c_init[:,col_index] = c_col
      return c_init


   def create_clusters(self):
      self.centroids = self.initialize_centroids()
      c_old = np.zeros(self.centroids.shape)
      c_c_dist = self.cal_distance(c_old, self.centroids)
      # np.any(c_c_dist) will return true if there is non-zero number in c_c_dist
      while np.any(c_c_dist):
         # Steps:
         # 1. iterate each point
         # 2. calculate the distance between the point and each centroid
         # 3. get the min distance
         # 4. assign the point to the centroid with the min distance
         # 5. store the centroids
         # 6. calculate average position of each cluster to determine new centroids
         for i in range(self.data_shape[0]):                                  # 1
            # dists: distances from the point to each centroid
            dists = self.cal_distance(self.data[i], self.centroids)           # 2
            # find the index of centroid which offers the min distance -> cluster label
            cluster_label = np.argmin(dists)                                  # 3
            self.cluster_labels[i] = cluster_label                            # 4
         c_old = deepcopy(self.centroids)                                     # 5
         for i in range(self.k):
            points_in_cluster_i = self.get_points_of_specific_cluster(i)
            if len(points_in_cluster_i) != 0:
               self.centroids[i] = np.mean(points_in_cluster_i, axis=0)       # 6
         c_c_dist = self.cal_distance(self.centroids, c_old)
      return self.centroids


   def get_points_of_specific_cluster(self, cluster_index):
      points = [self.data[p] for p in range(self.data_shape[0]) if self.cluster_labels[p] == cluster_index]
      return points


   # It will work iff input data is 1-D or 2-D. Otherwise it will print a warning
   def plot_clustering_result(self):
      if self.data.shape[1] > 2:
         print('Warning: Cannot plot the clustering result for points with more than 2 dimensions.')
         return
      plt.title('Clustering')
      # plot data points
      for i in range(self.k):
         points = self.get_points_of_specific_cluster(i)
         if self.data_shape[1] == 1:
            plt.scatter([x[0] for x in points], s=10)
         elif self.data_shape[1] == 2:
            plt.scatter([x[0] for x in points], [x[1] for x in points], s=10)
      # plot centroids (cluster points)
      for c in self.centroids:
         if self.data_shape[1] == 1:
            plt.scatter(c[0], 0, s=100, c='red',marker='*')
         elif self.data_shape[1] == 2:
            plt.scatter(c[0], c[1], s=100, c='red',marker='*')
      plt.show()



test = True
if test:
   # data = [[30,10], [25,15], [33,9],
   # [90,62], [85,77], [88, 69],
   # [55,29], [56,30], [55,30]]
   import csv
   csv_file = r'/home/vincentluo/Developing/Repos/Python_Repo/FancyPython/FancyLib/machine_learning/k-means_data.csv'
   csv_reader = csv.reader(open(csv_file, encoding='utf-8'))
   # data = [[float(x) for x in d] for d in list(csv_reader)]
   data = list(csv_reader)
   k = 3
   m = K_Means_Clustering(data, k)
   m.create_clusters()
   m.plot_clustering_result()