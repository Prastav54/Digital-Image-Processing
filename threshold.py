import numpy as np
from PIL import Image


def readImage(path):
    image = Image.open(path)
    image.show()
    return image


def threshold(image):
    th = int(input("Enter amount to threshold at: "))
    npImage = np.array(image)
    npImage = npImage > th
    npImage = npImage.astype(np.uint8) * 255
    newImage = Image.fromarray(npImage)
    newImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    threshold(im)
