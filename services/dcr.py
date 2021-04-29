import numpy as np
from sklearn.cluster import KMeans
import requests
from PIL import Image
import io
import time


def fetch_and_save_image(url: str) -> np.asarray:
    # ? Why was this necessary again ?
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


def get_dominant_colors(url: str, N_CLUSTERS=3) -> list:
    """
    Accepts an url (str) to an image.
    Retrieves the dominant colors through clustering.
    Returns the amount N_CLUSTERS colors within an array.
    """

    # Fetches image from url and saves it as a cv2 image object
    IMAGE = fetch_and_save_image(url)
    height, width, channels = IMAGE.shape

    # #  Checks if the image has color values
    assert channels == 3

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