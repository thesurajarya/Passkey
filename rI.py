from dotenv import load_dotenv
import os
import requests
from PIL import Image
import numpy as np
import random

load_dotenv() #from current directory
url = os.getenv("site_url")
# print(url)

def loadImage():
    try:
        with open("source.jpg","wb") as f:
            f.write(response.content)
        print("--> Image loaded successfully!")
    except Exception as e:
        print("--> Error loading image: ", e)

def imgArray(img_array):
    normalizedImgArray = (img_array / random.randint(1,100))
    # print(normalizedImgArray)
    print(normalizedImgArray.shape)
    return normalizedImgArray
# print(normalizedImgArray[0][1][0])

# request url for image
response = requests.get(url)

def openImg():
    img = Image.open("source.jpg")
    img_array = np.array(img)
    arr = {}
    return img_array

def matrixCalc(array, arr):
    for i in range(800):
        for j in range(600):
            arr[(i, j)] = array[i][j]   # tuple key (GOOD)

    finalArr = arr[(0, 0)].copy()

    for i in range(1, 800):
        for j in range(1, 600):
            finalArr += arr[(i, j)]

    print(finalArr)

def main():
    print("Generation phase 1 started...")
    loadImage()
    array = imgArray(openImg())
    arr = {}
    matrixCalc(array,arr)



if __name__ == "__main__":
    main()