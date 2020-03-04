import numpy as np
import cv2

# Load an color image in grayscale
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img = cv2.imread('Po2.jpg',1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()