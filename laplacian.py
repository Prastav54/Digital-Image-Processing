import numpy as np
from PIL import Image


def readImage(path):
    img = Image.open(path)
    return img


def applyFilter(npImage, filter_array):
    filter_size, _ = filter_array.shape
    num_rows, num_cols, m = npImage.shape
    padded = np.pad(npImage,
                    ((int((filter_size - 1) / 2), int((filter_size - 1) / 2)),
                     (int((filter_size - 1) / 2), int((filter_size - 1) / 2)),
                     (int((filter_size - 1) / 2), int((filter_size - 1) / 2)))
                    , 'constant')
    lst = []
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(m):
                window = padded[i:(filter_size + i), j:(filter_size + j), k:(filter_size + k)]

                r = 0
                # applying filter
                r = np.sum(np.multiply(filter_array, window))

                lst.append(r)
    newArray = np.resize(lst, (num_rows, num_cols, m))
    return newArray


def laplacian(img):
    npImage = np.array(img)
    filter_array = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])
    newArray = applyFilter(npImage, filter_array)
    newImage = Image.fromarray(newArray.astype(np.uint8))
    newImage.show()
    finalArr = npImage - newArray
    finalImage = Image.fromarray(finalArr.astype(np.uint8))
    finalImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    laplacian(im)
