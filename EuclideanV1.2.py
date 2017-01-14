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

r, c = 100, 2
results = [[0 for x in range(c)] for y in range(r)]

k = genfromtxt('eeg_demo.csv', delimiter=',')
k = np.ma.compress_cols(np.ma.masked_invalid(k))
# print(k[99][5])
l = k
k = k[:,0:len(k[0])-1]
# print(len(l[0]))
k_norm = preprocessing.scale(k)

dist_list = list()
# opt = optics(k_norm,0.1,5)
# opt.process()
# cluster = opt.get_clusters()
# noises = opt.get_noise()
# print(len(cluster))
# print((cluster))
# print(k_norm[1],'.',k_norm[2],'.',k_norm[19],'.',k_norm[4],'.',k_norm[5])
# print(len(noises))

count =1
arr = list()
label = list()
plt.figure("Humidity")
for num in range(0,500):
    arr.append(num)
    # label.append(l[num][15])
for row in k_norm:
    dist_list_row = list()
    val = distance.euclidean(row,k_norm[0])
    dist_list_row.append(val)
    dist_list.append(val)
    # plt.plot(arr, dist_list_row)
    # print(dist_list_row)

optics_instance = optics(dist_list,2.117,2)
optics_instance.process()

clusters = optics_instance.get_clusters()
noise = optics_instance.get_noise()
print("Clusters--",len(clusters))

cluster_index = 0
for c_in in range(0,len(clusters)):

    for label in clusters[c_in]:
        print(label, 'Label' , l[label][14],'Clustered to Index',c_in)
print(clusters)

print("--------------Clustering Results Writen to results.csv-------------")