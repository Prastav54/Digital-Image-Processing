import numpy as np
from PIL import Image


def readImage(path):
    image = Image.open(path)
    image.show()
    return image


def logTransform(image):
    c = float(input('Enter value of c:'))
    npImage = np.array(image)
    npImage = npImage / 255
    npImage = c * np.log(1 + npImage) * 255
    newImage = Image.fromarray(npImage.astype(np.uint8))
    newImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    logTransform(im)
