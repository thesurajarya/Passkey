from dotenv import load_dotenv
import os
import requests
from PIL import Image
import numpy as np
import random

load_dotenv() #from current directory
url = os.getenv("site_url")
key = os.getenv("dict")
# print(url)
# request url for image
response = requests.get(url)

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


def openImg():
    img = Image.open("source.jpg")
    img_array = np.array(img)
    img.close()
    return img_array

def matrixCalc(array, arr):
    for i in range(800):
        for j in range(600):
            arr[(i, j)] = array[i][j]   # tuple key (GOOD)

    finalArr = arr[(0, 0)].copy()

    for i in range(1, 800):
        for j in range(1, 600):
            finalArr += arr[(i, j)]

    return finalArr

def generatekey(ar_ray, length):
    mean = (np.mean(ar_ray)).astype(int)
    std = (np.std(ar_ray)).astype(int)
    passkey = ""
    passLength = f"{mean}{std}"
    print("\nMean: ",mean)
    print("Std: ",std)
    # while(len(passkey) < 12):
        
    #     passkey += key[]
    print("\nGenerated Passkey: ", passkey)
def main():
    print("Generation phase 1 started...")
    loadImage()
    array = imgArray(openImg())
    arr = {}
    print("\nGeneration phase 2 started...")
    generatekey(matrixCalc(array,arr), len(key))




if __name__ == "__main__":
    main()