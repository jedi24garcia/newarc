#!/usr/bin/env python3 

""" We are learning NumPy """

import numpy
from scipy import misc
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
# from numpy import linalg

img = imread('Tiger.jpg');
# img_gray = img_array @ [0.2126,  0.7152, 0.0722]
type(img)

numpy.ndarray
# img_gray.shape

# plt.imshow(img_gray, cmap="gray")
plt.imshow(img)
plt.show()
