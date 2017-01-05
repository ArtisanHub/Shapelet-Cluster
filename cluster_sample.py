 # example of clustering by BIRCH algorithm.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from numpy import genfromtxt
from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster.optics import optics
from pyclustering.samples.definitions import FCPS_SAMPLES
from pyclustering.utils import read_sample

# load data from the FCPS set that is provided by the library.
sample = read_sample(FCPS_SAMPLES.SAMPLE_LSUN)

# create BIRCH algorithm for allocation three objects.

k = genfromtxt('occu_demo_data.csv', delimiter=',')
k = np.ma.compress_cols(np.ma.masked_invalid(k))
# print(k)

# print(len(k[0]))
k = k[:,0:len(k[0])-1]
# np.delete(k_norm,2,axis=1)
k = preprocessing.scale(k)
optics_instance = optics(k, 0.5, 10)

optics_instance.process()

clusters = optics_instance.get_clusters()

noise = optics_instance.get_noise()
ordering = optics_instance.get_cluster_ordering()

indexes = [i for i in range(0, len(ordering))]

plt.bar(indexes, ordering)
plt.show()