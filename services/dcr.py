# Comments @ get_dominant_colors-----------------------------
# ! Function doesn't filter out the white background-color that most logos have.
# TODO: Filter out the white color values before applying clustering.
# ? Write a new function to filter out the white background color?

# ! The amount of colors to be returned is currently set to 3.
# TODO: Research how much colors the logo's have on average.
# TODO: Discuss with front-end developers how many colors they would like to be able to extract.
# ? Add N_CLUSTERS params to this function?

# !: Assertion check doesn't seem to work. " AssertionError "
# TODO: Fix the assertion check.

# !: Clusters aren't sorted (=> colors aren't sorted.)
# TODO: Sort the cluster centers before returning the list.
# -----------------------------------------------------------


import numpy as np
from sklearn.cluster import KMeans
import requests
from PIL import Image
import io
import time


def fetch_and_save_image(url: str) -> np.asarray:
    """
    Fetches the image from the url
    Loads the image as a CV2 Image object
    Returns a cv2.Image object
    """

    response = requests.get(url)
    image_bytes = io.BytesIO(response.content)

    PIL_IMG = Image.open(image_bytes)
    IMG = np.asarray(PIL_IMG)

    return IMG


def rgb_to_hex(rgb: tuple) -> str:
    """
    Accepts a tuple of RGB values (R: int, G: int, B: int)
    Turns the rgb values to a hexadecimal value.
    Returns the hexadecimal value as a string.
    """

    return '%02x%02x%02x' % rgb


def get_dominant_color(url: str) -> list:
    """
    Accepts an url (str) to an image.
    Retrieves the dominant colors through clustering.
    Returns the amount N_CLUSTERS colors within an array.
    """
    N_CLUSTERS = 3

    # Fetches image from url and saves it as a cv2 image object
    IMAGE = fetch_and_save_image(url)
    height, width, channels = IMAGE.shape

    # // Checks if the image has color values
    # // assert channels == 3

    # Reshaping the image array for the KMeans algorithm
    IMAGE = IMAGE.reshape((height * width), channels)

    # Clustering the image
    IMG_CLUSTER = KMeans(n_clusters=N_CLUSTERS).fit(IMAGE)

    # Contains the dominant colors of the image
    CLUSTER_CENTERS = IMG_CLUSTER.cluster_centers_

    # An empty list in which the color values will be put into.
    rgb_hex_values = []

    for i in range(N_CLUSTERS):
        # Determines the RGB value of every cluster
        RGB = (round(CLUSTER_CENTERS[i][0]), round(
            CLUSTER_CENTERS[i][1]), round(CLUSTER_CENTERS[i][2]))

        # Appends the RGB-turned Hex values to the rgb_hex_values list
        rgb_hex_values.append((rgb_to_hex(RGB)))

    return rgb_hex_values


# ! @ PEER REVIEWERS
# ! uncomment the code below and run this file to see the results.

# For testing the time it takes for the get_dominant_colors() function to run.
# @ Reviewers, uncomment and run this file to see the results.
# test_url = "http://dashboard-pio.herokuapp.com/companyLogos/Fynch.png"
# start_time = time.time()
# print(get_dominant_color(test_url))
# print(f'time it took to run get_dominant_color in seconds: {time.time() - start_time}')
