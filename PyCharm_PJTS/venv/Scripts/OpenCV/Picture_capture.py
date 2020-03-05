import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Media/Po2.jpg', 1)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()


# px = img[100:300,100:500] #returns an array of Blue, Green, Red values
# print(px)
# print(img.item(10,10,2)) #

# accessing RED value
# img.item(10,10,2)

# modifying RED value
# img.itemset((50,50,2),100)
# img.item(10,10,2)
#
# print(img.size) # pixels qty
# print(img.dtype)

           #x  y точки 1
ball = img[405:283, 330:390]
           #x  y точки 2
img[273:333, 100:160] = ball

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
