from dotenv import load_dotenv
import os
import requests
from PIL import Image
import numpy as np
import random

load_dotenv() #from current directory

url = os.getenv("site_url")
print(url)

response = requests.get(url)
try:
    with open("source.jpg","wb") as f:
        f.write(response.content)
    print("Image loaded successfully!")
except Exception as e:
    print("Error loading image: ", e)

img = Image.open("source.jpg")
img_array = np.array(img)
normalizedImgArray = (img_array / random.randint(1,100))
print(normalizedImgArray)