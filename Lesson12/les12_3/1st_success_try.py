from skimage.io import imread, imsave
import numpy as np
import os

img1 = imread('1.png')
img2 = imread('2.png')


img1 = np.array([[a + b for a, b in zip(row, other_row)] for row, other_row in zip(img1, img2)])


imsave('original' + '.png', img1)
os.remove('1.png')
os.remove('2.png')
