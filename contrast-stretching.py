import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def readImage(path):
    image = Image.open(path)
    image.show()
    return image


def contrastStretching(image):
    # convert to numpy array
    npImage = np.array(image)
    orgImage = npImage
    minimum = npImage.min()
    maximum = npImage.max()
    diff = maximum - minimum
    npImage = (npImage - minimum) / diff * 255
    newImage = Image.fromarray(npImage.astype(np.uint8))
    newImage.show()
    fig = plt.figure()
    fig.add_subplot(2, 1, 1)
    plt.hist(orgImage.flatten(), bins=50)
    fig.add_subplot(2, 1, 2)
    plt.hist(npImage.flatten(), bins=50)
    plt.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    contrastStretching(im)
