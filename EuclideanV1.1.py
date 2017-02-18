from pyclustering.cluster.optics import optics
from sklearn import preprocessing
from numpy import genfromtxt
from scipy.spatial import distance


import numpy as np


output_file_with_clusters_ = ""  #Provide the filename where the output needs to be written


def cluster_algo(r,c,eps,min_pts,dataset_name):

    results = [[0 for x in range(c)] for y in range(r)]

    # dataset to be clustered based on euclidean distance

    k = genfromtxt(dataset_name, delimiter=',')
    k = np.ma.compress_cols(np.ma.masked_invalid(k))
    l = k

    # normalization
    k = k[:, 0:len(k[0]) - 1]
    k_norm = preprocessing.scale(k)

    dist_list = list()

    count = 1
    for row in k_norm:
        dist_list_row = list()
        for row1 in k_norm:
            val = distance.euclidean(row, row1)
            dist_list_row.append(val)
        dist_list.append(dist_list_row)

        # Clustering the distance matrix based on the OPTICS algo
        optics_instance = optics(dist_list_row, eps, min_pts)
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

        # Assigning each time instance to a cluster
        clusterCount = 1
        for k in clusters:
            for temp in k:
                if clusterCount <= c:
                    results[temp][clusterCount - 1] = results[temp][clusterCount - 1] + 1

                else:
                    results[temp][c - 1] = results[temp][c - 1] + 1

            clusterCount = clusterCount + 1

        print("Number of clusters")
        print(clusterCount - 1)

    print("--------------Clustering Results-------------")

    print(len(results))
    output = open(output_file_with_clusters_, 'w')
    c = 0
    tempRowNum = 1
    for row in results:
        print("row: " + str(tempRowNum) + " ****has count of cluster 0: " + str(
            row[0]) + " ****has count of cluster 1: " + str(row[1]))

        output.write(str(tempRowNum))
        output.write(str(","))
        output.write(str(row.index(max(row))))
        output.write(str("\n"))
        tempRowNum = tempRowNum + 1

    output.close()

    print("--------------Clustering Results Writen to results.csv-------------")

