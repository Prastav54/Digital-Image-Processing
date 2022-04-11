import numpy as np
from PIL import Image


def readImage(path):
    image = Image.open(path)
    image.show()
    return image


def bitPlaneSlicing(image, bit):
    if bit < 1 or bit > 8:
        print("Error in bit")
        return 0
    npImage = np.array(image)
    masks = [1, 2, 4, 8, 16, 32, 64, 128]
    num_rows, num_cols, a = np.squeeze(npImage.shape)
    npMask = np.full((num_rows, num_cols, a), masks[bit - 1])
    npImage = npImage & npMask
    newImage = Image.fromarray(npImage.astype(np.uint8))
    newImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    for i in range(1, 9):
        bitPlaneSlicing(im, i)
