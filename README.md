# Shapelet-Cluster
Unsupervised Learning clustering technique is implemented in order to label a given unlabeled dataset.
Output of the implementation will provide a classify each time instance of a multivariate time series dataset. 

# How to run
Function named cluster_algo(r,c,eps,min_pts,dataset_name) has to be called passing the necessary parameters.
  r - Number of rows of the total dataset
  c - Expected number of events/clusters the multivariate time series is expected to be clustered to
  eps - maximum radius to be considered with respect to a given data point in defining cluster boundary
  min_pts - minimum number of points within a cluster
  dataset_name - provide the obtained dataset file name

# Important
The technique only facilitates numeric datasets
The accuracy of the clustering technique will be varied upon the values passed for eps, min_pts

# Testing
In order to test the approach we have used following labeled datasets and prepared the dataset file without the annotated column
and compared the results obtained from our implementation against the actual annotation.
  Occupancy Detection Dataset - https://archive.ics.uci.edu/ml/datasets/Occupancy+Detection+
  EEG-Eye State Dataset - https://archive.ics.uci.edu/ml/datasets/EEG+Eye+State
  
