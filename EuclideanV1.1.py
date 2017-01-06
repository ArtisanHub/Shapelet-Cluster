from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster.birch import birch
from pyclustering.cluster.optics import optics
from pyclustering.utils import draw_clusters
from sklearn import preprocessing
from sklearn.cluster import DBSCAN
from numpy import genfromtxt
from scipy.spatial import distance
import math
import numpy as np
import matplotlib.pyplot as plt

r, c = 20, 2
results = [[0 for x in range(c)] for y in range(r)]

tempClusterCount = 0

k = genfromtxt('occu_demo_data.csv', delimiter=',')
k = np.ma.compress_cols(np.ma.masked_invalid(k))
# print(k)

# print(len(k[0]))
k = k[:,0:len(k[0])-1]
# np.delete(k_norm,2,axis=1)
k_norm = preprocessing.scale(k)

dist_list = list()
# Got the whole data set to a list.
count =1
for row in k_norm:
    dist_list_row = list()
    for row1 in k_norm:
        val = distance.euclidean(row,row1)
        dist_list_row.append(val)
    dist_list.append(dist_list_row)
    # print(dist_list_row)

    optics_instance = optics(dist_list_row,0.2117,1)
    print ("Distance for row ")
    print(count)
    count = count + 1
    print(dist_list_row)
    optics_instance.process()

    clusters = optics_instance.get_clusters()
    print("Clusters")
    print(clusters)
    # print("Cluster Points")
    # print(len(clusters))
    noise = optics_instance.get_noise()
    print("Noise")
    print(noise)

    clusterCount = 0
    for k in clusters:
       for temp in k:
           if clusterCount == 0 or clusterCount == 1:
               #print("####### " + str(temp) + " ######### " + str(clusterCount))
               results[temp][clusterCount]  = results[temp][clusterCount] + 1

           else:
               continue

       clusterCount = clusterCount + 1

print(results)