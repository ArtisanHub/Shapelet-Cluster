
from sklearn import preprocessing
from statsmodels.nonparametric.kde import KDEUnivariate
from sklearn.neighbors.kde import KernelDensity
from numpy import genfromtxt
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

r, c = 100, 2

k = genfromtxt('occu_demo_data.csv', delimiter=',')
k = np.ma.compress_cols(np.ma.masked_invalid(k))
l = k
k = k[:,0:len(k[0])-1]

k_norm = preprocessing.scale(k)

dist_list = list()


count =1
arr = list()
label = list()
for num in range(0,500):
    arr.append(num)
    # label.append(l[num][15])
for row in k_norm:
    dist_list_row = list()
    val = distance.euclidean(row,k_norm[0])
    dist_list_row.append(val)
    dist_list.append(val)

#Now Have the Distances list w.r.t t the first row.
# print(dist_list)
np.asarray(dist_list)
# print(dist_list)
dist_list = np.reshape(dist_list,(500,1))
# print(dist_list)
# dist_list = np.array([10, 11, 9, 23, 21, 11, 45, 20, 11, 12]).reshape(-1, 1)
kde = KernelDensity(kernel='gaussian',bandwidth=10).fit(dist_list)
s = np.linspace(0, 500,500)
print(len(s))
e = kde.score_samples(dist_list)
# print(e)
plt.plot(s,e)
plt.show()
from scipy.signal import argrelextrema
mi, ma = argrelextrema(e, np.less)[0], argrelextrema(e, np.greater)[0]
# print(len(mi))
# print(len(ma))
# print ("Minima:", s[mi])
# print ("Maxima:", s[ma])
print(mi[0])
print (len(dist_list[dist_list< mi[0]]), len(dist_list[(dist_list >= mi[0]) * (dist_list<= mi[1])]), len(dist_list[dist_list >= mi[1]]))
plt.plot(s[:mi[0] + 1], e[:mi[0] + 1], 'r',
     s[mi[0]:mi[1] + 1], e[mi[0]:mi[1] + 1], 'g',
     s[mi[1]:], e[mi[1]:], 'b',
         s[ma], e[ma], 'go',
         s[mi], e[mi], 'ro')

plt.show()