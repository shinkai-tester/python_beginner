from skimage.io import imread, imsave
import numpy as np
import os

img1 = imread('1.png')
img2 = imread('2.png')
img1_copy = np.array(img1)
img2_copy = np.array(img2)
original = img1_copy + img2_copy

imsave('original' + '.png', original)
os.remove('1.png')
os.remove('2.png')
