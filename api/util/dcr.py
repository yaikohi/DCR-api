import json
import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import requests
from PIL import Image
import io


def convert_from_pil_to_cv2(img: Image) -> np.asarray:
    return np.asarray(img)


def fetch_and_save_image(url: str) -> np.asarray:
    response = requests.get(url)
    image_bytes = io.BytesIO(response.content)

    PIL_IMG = Image.open(image_bytes)
    IMG = convert_from_pil_to_cv2(PIL_IMG)

    return IMG 

def rgb_to_hex(rgb: tuple) -> str:
    return '%02x%02x%02x' % rgb



def get_dominant_color(url: str) -> list:
    """
    input:
    url: url from the logo dict

    output: list with hex values
    """
    # AMOUNT OF CLUSTERS = 3
    N_CLUSTERS = 3

    # Fetches image from url and saves it as a cv2 image object
    IMAGE = fetch_and_save_image(url)

    height, width, channels = IMAGE.shape

    # TODO: Fix the assertion check.
    # !: Assertion check doesn't seem to work. " AssertionError "
    # Checks if the image has color values
    # assert channels == 3

    # Reshaping the image array for the KMeans algorithm
    IMAGE = IMAGE.reshape((height * width), channels)

    # Clustering the image
    IMG_CLUSTER = KMeans(n_clusters = N_CLUSTERS).fit(IMAGE)

    # TODO: Sort the cluster centers.
    # !: Clusters aren't sorted (=> colors aren't sorted.)
    # Contains the dominant colors of the image
    CLUSTER_CENTERS = IMG_CLUSTER.cluster_centers_

    # init empty list for output
    rgb_hex_values = []

    for i in range(N_CLUSTERS):
        RGB = (round(CLUSTER_CENTERS[i][0]), round(CLUSTER_CENTERS[i][1]), round(CLUSTER_CENTERS[i][2]))

        rgb_hex_values.append((rgb_to_hex(RGB)))
    
    return rgb_hex_values