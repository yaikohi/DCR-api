# Color palette extraction tutorial: https://towardsdatascience.com/color-palette-extraction-with-k-means-clustering-machine-learning-from-scratch-part-iv-55e807407e53
# Means Color Clustering tutorial: https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/#:~:text=K%2Dmeans%20is%20a%20clustering,cluster%20with%20the%20nearest%20mean.&text=Pixels%20that%20belong%20to%20a,belonging%20to%20a%20separate%20cluster.

# EXTERNAL LIBRARY IMPORTS
from matplotlib import pyplot as plt

# from scipy.cluster.vq import kmeans, vq
from sklearn.cluster import KMeans

import numpy as np
import pandas as pd
import argparse
import cv2


from utils import centroid_histogram, plot_colors

# VARIABLE IMPORTS
from preprocessing.data_processing import *

#__________________________________________________________________________

# Argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-c", "--clusters", required = True, type = int, help = "Number of clusters")
args = vars(ap.parse_args())

IMG = cv2.imread(args["image"])
IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2RGB)


#__________________________________________________________________________
# TODO: Write functions for the processing methods
# TODO: Write the code to take in an URL instead of a filelocation


# Path variables
COLOR_LABELS_PATH = "./data/csv/colors.csv"
# moved from "../preprocessing/readability"
IMG_DB = ".../testdata/json/db_full_logo_urls.json"

#__________________________________________________________________________



# Data

## Loading the image

IMG = cv2.imread(args["image"])             # Loads the image (BGR) with dtype = numpy.ndarray
IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2RGB)  # Converting the image colours from BGR to RGB

# IMG = cv2.imread(IMG_PATH)                  
# IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2RGB) 

dimensions = IMG.shape                      # 466 rows, 640 columns, 3 channels. dtype = tuple
height, width, channels = dimensions        # Unpacking the tuple into variables. Each variable has INT dtype.
assert channels == 3                        # Checks if the image has color channels.
area = height * width                       # 466 * 640 = 298240 pixels

#__________________________________________________________________________

# @WHAT: Reshaping the image for kmeans clustering.
# @WHY: kmeans clustering requires a 2d list. Since cv2 retrieves a 3d list when loading an image, 
# a reshape method has to be applied.
# @ALTERNATIVES: changing the data with different methods.
IMG = IMG.reshape((height * width, channels))

#__________________________________________________________________________


## Clustering
clt = KMeans(n_clusters = args["clusters"])
clt.fit(IMG)

hist = centroid_histogram(clt)
bar = plot_colors(hist, clt.cluster_centers_)
# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()

#__________________________________________________________________________
# print(len(np.unique(clt.labels_)))                      # 4

# n_labels = np.arange(0, len(np.unique(clt.labels_))+1)  # [0 1 2 3 4]
# (hist, _) = np.histogram(clt.labels_, bins=n_labels)
# hist.astype("float")
# print(hist)
# print(hist.sum())

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color

#__________________________________________________________________________


# ## Color labels dataframe
# index = ["color", "color_name", "hex", "R", "G", "B"]
# COLOR_LABELS_DF = pd.read_csv("colors.csv", names=index, header=None)

#__________________________________________________________________________


# print(color_labels_df)

# figure = plt.figure()
# ax = figure.add_subplot(111, projection='3d')

# x = 
# y = 
# z = 