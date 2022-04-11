import numpy as np
from PIL import Image


def readImage(path):
    image = Image.open(path)
    image.show()
    return image


def applyFilter(npImage, filter_array, typeOfFilter="weight"):
    filter_size, _ = filter_array.shape
    num_rows, num_cols = npImage.shape
    padded = np.pad(npImage,
                    ((int((filter_size - 1) / 2), int((filter_size - 1) / 2)),
                     (int((filter_size - 1) / 2), int((filter_size - 1) / 2)))
                    , 'constant')
    lst = []
    for i in range(num_rows):
        for j in range(num_cols):
            window = padded[i:(filter_size + i), j:(filter_size + j)]

            r = 0
            # applying filter
            if typeOfFilter == "weight":
                r = np.sum(np.multiply(filter_array, window))
            elif typeOfFilter == "median":
                r = np.median(window)

            lst.append(r)
    newArray = np.resize(lst, (num_rows, num_cols))
    return newArray


def highBoost(img):
    npImage = np.array(img)
    filter_size = int(input("Enter filter size:"))
    filter_array = []
    for i in range(filter_size):
        for j in range(filter_size):
            weight = float(input("Enter weight[{}][{}]:".format(i, j)))
            filter_array.append(weight)
    A = float(input("Enter amplification factor:"))
    filter_array = np.resize(filter_array, (filter_size, filter_size))
    newArray = applyFilter(npImage, filter_array)
    newArray = (A - 1) * npImage + newArray
    newImage = Image.fromarray(newArray.astype(np.uint8))
    newImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    highBoost(im)
