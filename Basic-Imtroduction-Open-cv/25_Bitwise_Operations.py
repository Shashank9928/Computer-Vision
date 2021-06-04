import cv2 as cv
import numpy as np
img1 = np.zeros([200,400,3],np.uint8)
img1 = cv.rectangle(img1,(100,25),(300,150),(255,255,255),-1)

img2 = cv.imread("Images/BlackWhite.jpg")
### TODO: And Operator
# img3 = cv.bitwise_and(img1,img2)
### TODO: Or Operator
# img3 = cv.bitwise_or(img1,img2)
### TODO: Not Operator
# img3 = cv.bitwise_not(img2)
### TODO: Xor Operator
# img3 = cv.bitwise_xor(img1,img2)
# cv.imshow("1",img1)
# cv.imshow("2",img2)
cv.imshow("Bitwise Operation",img3)
cv.waitKey(0)
cv.destroyAllWindows()
