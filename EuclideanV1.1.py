from sklearn import preprocessing
from numpy import genfromtxt
from scipy.spatial import distance
import math
import numpy as np


k = genfromtxt('occu_demo_data.csv', delimiter=',')
k = np.ma.compress_cols(np.ma.masked_invalid(k))
# print(k)

# print(len(k[0]))
k = k[:,0:len(k[0])-1]
# np.delete(k_norm,2,axis=1)
k_norm = preprocessing.scale(k)


print("Euclidean Similarity \n")

unit_normal = list()
for x in range(0,len(k)-1):
   for y in range(0,len(k)-1):
       # print(y)
       if(distance.euclidean(k_norm[x],k_norm[y]) < 1 ):
           print(distance.euclidean(k_norm[x],k_norm[y]))
           print("Event 1")

       else :
           print(distance.euclidean(k_norm[x],k_norm[y]))
           print("Event 2" )



# print("Cosine Similarity \n")
# print(distance.cosine(k_norm[0],k_norm[0]))
# print(distance.cosine(k_norm[0],k_norm[7]))
# print(k_norm)

