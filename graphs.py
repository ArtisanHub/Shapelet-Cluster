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

col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
row_numbers = []

k = genfromtxt('occu_demo_data.csv', delimiter=',')
k = np.ma.compress_cols(np.ma.masked_invalid(k))

k = k[:,0:len(k[0])-1]

k_norm = preprocessing.scale(k)
# k_norm.diff(k_norm)
row_num = 1
count = 0

arr = list()
for row in k_norm:

    row_numbers.append(count+1)
    col1.append(row[0])
    col2.append(row[1])
    col3.append(row[2])
    col4.append(row[3])
    col5.append(row[4])
    row_num = row_num + 1
    count = count + 1
arr.append(0)
arr = np.diff(col1)
# arr.put(99,0)
print(len(arr))
print(len(row_numbers))
plt.figure("Humidity")
plt.plot(row_numbers, col1)

plt.figure("Light")
row_numbers.pop(99)
plt.plot(row_numbers, arr)
row_numbers.append(100)
plt.figure("co2")
plt.plot(row_numbers, col3)

plt.figure("HumidityRatio")
plt.plot(row_numbers, col4)

plt.figure("Occupancy")
plt.plot(row_numbers, col5)

plt.show()