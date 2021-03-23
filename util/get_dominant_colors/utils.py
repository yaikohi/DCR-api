# import the necessary packages
import numpy as np
import cv2

# def centroid_histogram(clt):
# 	# grab the number of different clusters and create a histogram
# 	# based on the number of pixels assigned to each cluster

#     unique_labels = np.unique(clt.labels_)
#     n_unique_labels = len(unique_labels)
    
#     n_labels = np.arange(0, n_unique_labels+1)
#     # The underscore means that we're not interested in this value ("bin_edges", array with dtype float) that np.histogram also returns.
#     (hist, _) = np.histogram(clt.labels_, bins=n_labels)


#     # normalize the histogram, such that it sums to one
#     hist = hist.astype("float")
#     hist /= hist.sum()
#     # return the histogram
#     return hist


def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    n_labels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    
    # @WHAT: (hist, _)
    # @WHY: The underscore means that we're not interested in this value ("bin_edges", array with dtype float)
    #  that np.histogram also returns.
    (hist, _) = np.histogram(clt.labels_, bins = n_labels)

    # @WHAT: normalizes the data by dividing it by the sum of the data
    # @WHY: so that variance is respected
    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")

    # @WHAT: Divides hist by hist.sum()
    # @WHY: ...?
    hist /= hist.sum()
    # return the histogram
    return hist


def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
	# of each of the colors
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
            color.astype("uint8").tolist(), -1)
        startX = endX
	
    # return the bar chart
    return bar