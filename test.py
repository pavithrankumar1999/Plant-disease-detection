import cv2
import numpy as np
DATA = cv2.imread('test_im.jpg')
new = cv2.resize(DATA , (50,50))