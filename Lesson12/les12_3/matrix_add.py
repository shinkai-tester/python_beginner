from skimage.io import imread, imsave
import numpy as np
import os


def addMatrix(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        res.append(row)
    res = np.array(res)
    return res


img1 = imread('1.png')
img2 = imread('2.png')
imsave('original' + '.png', addMatrix(img1, img2))
os.remove('1.png')
os.remove('2.png')
