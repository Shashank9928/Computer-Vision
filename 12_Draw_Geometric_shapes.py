import cv2 as cv

img = cv.imread("Images\Lena.png",1)

img = cv.line(img,(0,128),(128,128),(255,0,0),5)
img = cv.arrowedLine(img,(0,0),(128,128),(0,0,255),10)

cv.imshow("Geometry_Shape",img)
cv.waitKey(0)
cv.destroyAllWindows()