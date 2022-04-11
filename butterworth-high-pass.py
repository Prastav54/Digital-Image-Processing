from math import floor, sqrt, exp
from scipy import fftpack
import numpy as np
from PIL import Image


def readImage(path):
    img = Image.open(path)
    return img


def shiftXY(npArr):
    rows, cols, m = npArr.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(m):
                npArr[i][j][k] = npArr[i][j][k] * ((-1) ** (i + j + k))  # f(x,y) * (-1)^(x+y)
    return npArr


def butterworthHPF(image):
    npImage = np.array(image)
    cutoff = float(input("Enter cutoff radius:"))
    n = int(input("Enter order of filter:"))
    npImage = shiftXY(npImage)
    fft = fftpack.fftshift(fftpack.fft2(npImage))
    rows, cols, m = fft.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(m):
                duv = sqrt(i * i + j * j + k * k)  # D(u,v)=sqrt(u^2+v^2)
                if duv == 0:
                    duv = 0.0001
                hpf = 1 / (1 + (cutoff / duv) ** (2 * n))
                fft[i][j][k] = hpf * fft[i][j][k]
    ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(fft)))
    ifft2 = np.maximum(0, np.minimum(ifft2, 255))
    magnitude_spectrum = 20 * np.log(np.abs(ifft2))
    magnitude_spectrum = shiftXY(magnitude_spectrum)
    newImage = Image.fromarray(magnitude_spectrum.astype(np.uint8))
    newImage.show()


if __name__ == '__main__':
    im = readImage("dog.jpg")
    butterworthHPF(im)
