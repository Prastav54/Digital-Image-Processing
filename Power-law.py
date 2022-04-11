import numpy as np
from PIL import Image


def readImage(path):
    image = Image.open(path)
    image.show()
    return image


def powerLaw(image):
    c = float(input('Enter value of c:'))
    g = float(input('Enter value of gamma:'))
    npImage = np.array(image)
    npImage = npImage / 255
    npImage = c * np.power(npImage, g) * 255
    newImage = Image.fromarray(npImage.astype(np.uint8))
    newImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    powerLaw(im)
