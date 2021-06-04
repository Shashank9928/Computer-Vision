import numpy as np
import cv2 as cv

img =cv.imread("Images\Ball.jpg")
# img = cv.rectangle(img,(450,205),(700,450),(255,0,0),thickness = 5)
# img = cv.rectangle(img,(10,10),(255,250),(0,0,255),thickness = 5)

my_img = img[205:445,450:695]
img[10:250,10:255] = my_img
# cv.imshow("MY_IMG",my_img)
cv.imshow("IMAGE",img)
cv.waitKey(0)
cv.destroyAllWindows()