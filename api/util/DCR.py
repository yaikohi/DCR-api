import json
import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import requests
from PIL import Image
import io


# For testing purposes
DB = "../data/db_full_logo_urls.json"
data = json.load(open(DB))

N_CLUSTERS: int = 3
RGB_VALUES = []



def get_dominant_color(company_data_json, company_name: str) -> list:
    logo_url = company_data_json[company_name]['logo']
    IMAGE = fetch_and_save_image(logo_url)

    height, width, channels = IMAGE.shape
    assert channels == 3
    IMAGE = IMAGE.reshape((height * width), channels)

    IMG_CLUSTER = KMeans(n_clusters = N_CLUSTERS).fit(IMAGE)
    CLUSTER_CENTERS = IMG_CLUSTER.cluster_centers_

    rgb_hex_values = []

    for i in range(N_CLUSTERS):
        RGB = (round(CLUSTER_CENTERS[i][0]), round(CLUSTER_CENTERS[i][1]), round(CLUSTER_CENTERS[i][2]))

        rgb_hex_values.append((rgb_to_hex(RGB)))
    
    return rgb_hex_values
