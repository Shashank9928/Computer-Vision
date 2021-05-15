import cv2 as cv

img = cv.imread("Images\Lena.png",1)
img = cv.rectangle(img,(50,128),(128,150),(255,0,0),thickness = 5)

#### Fill the rectangle
# img = cv.rectangle(img,(50,128),(128,150),(255,0,0),-1)

cv.imshow("Rectangle",img)
cv.waitKey(0)
cv.destroyAllWindows()