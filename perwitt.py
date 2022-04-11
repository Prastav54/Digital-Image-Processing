import numpy as np
from PIL import Image


def readImage(path):
    image = Image.open(path)
    image.show()
    return image


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


def prewitt(img):
    npImage = np.array(img)
    filter_array_row = np.array([[-1, -1, -1],
                                 [0, 0, 0],
                                 [1, 1, 1]])
    filter_array_col = np.array([[-1, 0, 1],
                                 [-1, 0, 1],
                                 [-1, 0, 1]])
    newArray_row = applyFilter(npImage, filter_array_row)
    newImage = Image.fromarray(newArray_row.astype(np.uint8))
    newImage.show()
    newArray_col = applyFilter(npImage, filter_array_col)
    newImage = Image.fromarray(newArray_col.astype(np.uint8))
    newImage.show()
    newArray = newArray_row + newArray_col
    newImage = Image.fromarray(newArray.astype(np.uint8))
    newImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    prewitt(im)
