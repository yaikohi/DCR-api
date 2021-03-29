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