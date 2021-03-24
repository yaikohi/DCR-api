"""
Removes the white pixels from a loaded/decoded image.
"""

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


def fetch_and_save_image(url: str) -> Image:
    response = requests.get(url)
    image_bytes = io.BytesIO(response.content)

    PIL_IMG = Image.open(image_bytes)
    IMG = convert_from_pil_to_cv2(PIL_IMG)

    return IMG 


def remove_white(img: Image) -> Image:
    pixels = img.load()
    
    R, G, B = img.convert("RGB" ).split()

    height, width, channels = img.shape
    assert channels == 3
    IMAGE = img.reshape((height * width), channels)