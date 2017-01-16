
from pyclustering.cluster.optics import optics
from sklearn import preprocessing
from numpy import genfromtxt
from scipy.spatial import distance

import numpy as np

import sys

r, c = int(sys.argv[1]), int(sys.argv[2])
results = [[0 for x in range(c)] for y in range(r)]

k = genfromtxt('iris_data.csv', delimiter=',')
k = np.ma.compress_cols(np.ma.masked_invalid(k))
l = k
k = k[:,0:len(k[0])]

k_norm = preprocessing.scale(k)

dist_list = list()

count =1
for row in k_norm:
    dist_list_row = list()
    for row1 in k_norm:
        val = distance.euclidean(row,row1)
        dist_list_row.append(val)
    dist_list.append(dist_list_row)

    optics_instance = optics(dist_list_row, float(sys.argv[3]), int(sys.argv[4]))
    print("Distance for row ")
    print(count)
    count = count + 1
    print(dist_list_row)
    optics_instance.process()

    clusters = optics_instance.get_clusters()
    print("Clusters")
    print(clusters)

    noise = optics_instance.get_noise()
    print("Noise")
    print(noise)

    clusterCount = 1
    for k in clusters:
       for temp in k:
           if clusterCount <= c:
               results[temp][clusterCount-1]  = results[temp][clusterCount-1] + 1

           else:
               results[temp][c-1] = results[temp][c-1] + 1
               #continue

       clusterCount = clusterCount + 1

    print("Number of clusters")
    print(clusterCount-1)

print("--------------Clustering Results-------------")


output = open('D:/FYP-Developments/Shapelet-Cluster/results.csv', 'w')


print(len(results))
output = open('results.csv', 'w')
c = 0
tempRowNum = 1
for row in results:
    print("row: " + str(tempRowNum) + " ****has count of cluster 1: " + str(row[0]) + " ****has count of cluster 2: " + str(row[1])
          + " ****has count of cluster 3: " + str(row[2]))
    if (row[0] >= row[1]) and (row[0] > row[2]):
        output.write(str(tempRowNum))
        output.write(str(","))
        output.write(str(1))

    elif (row[1] > row[0]) and (row[1] >= row[2]):
        output.write(str(tempRowNum))
        output.write(str(","))
        output.write(str(2))

    else:
        output.write(str(tempRowNum))
        output.write(str(","))
        output.write(str(3))

    output.write(str("\n"))
    tempRowNum = tempRowNum + 1

output.close()

print("--------------Clustering Results Writen to results.csv-------------")