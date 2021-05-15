import cv2 as cv

img = cv.imread("Images\Lena.png",1)
img = cv.circle(img,(128,128),50,(255,0,0),thickness=7)

#### Fill the Circle
# img = cv.circle(img,(128,128),50,(255,0,0),-1)

cv.imshow("Rectangle",img)
cv.waitKey(0)
cv.destroyAllWindows()