import numpy as np
from PIL import Image


def readImage(path):
    image = Image.open(path)
    image.show()
    return image


def negative(image):
    # convert to numpy array
    npImage = np.array(image)
    maximum = npImage.max()  # get the maximum
    newImage = Image.fromarray(maximum - npImage)  # subtract from maximum and convert back to image
    newImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    negative(im)
