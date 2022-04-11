import numpy as np
from PIL import Image


def readImage(path):
    image = Image.open(path)
    image.show()
    return image


def grayLevelSlicing(image):
    boostValue = 100
    minLevel = int(input('Enter minimum value:'))
    maxLevel = int(input('Enter maximum value:'))
    npImage = np.array(image)

    # fully suppress other levels
    npImage = np.where((npImage > minLevel) & (npImage < maxLevel), npImage + boostValue, 20)
    npImage = np.where(npImage > 255, 255, npImage)
    newImage = Image.fromarray(npImage.astype(np.uint8))
    newImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    grayLevelSlicing(im)
