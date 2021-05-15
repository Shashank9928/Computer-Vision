import numpy as np
import cv2 as cv

img = cv.imread("Images/Gradient.jpg")

# _,th0 = cv.threshold(img,50,255,cv.THRESH_BINARY)
# _,th0 = cv.threshold(img,50,255,cv.THRESH_BINARY_INV)
# _,th0 = cv.threshold(img,50,255,cv.THRESH_TRUNC)
# _,th0 = cv.threshold(img,50,255,cv.THRESH_TOZERO)
_,th0 = cv.threshold(img,50,255,cv.THRESH_TOZERO_INV)

cv.imshow("Original Image",img)

cv.imshow("TRESHOLD IMG",th0)

cv.waitKey(0)
cv.destroyAllWindows()