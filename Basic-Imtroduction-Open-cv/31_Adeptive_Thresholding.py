import numpy as np
import cv2 as cv
img = cv.imread("Images/Calendar-2.jpg",0)
_,th1 = cv.threshold(img,100,255,cv.THRESH_BINARY)

#### ADAPTIVE THRESHHOLD BINERY WITH MEAN METHORD
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

#### ADAPTIVE THRESHHOLD BINERY WITH GAUSSIAN METHORD
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow("Iamge",img)
cv.imshow("THRESHOLD IMG",th1)
cv.imshow("MEAN THRESHOLD IMG",th2)
cv.imshow("GAUSSIAN THRESHOLD IMG",th3)

cv.waitKey(0)
cv.destroyAllWindows()