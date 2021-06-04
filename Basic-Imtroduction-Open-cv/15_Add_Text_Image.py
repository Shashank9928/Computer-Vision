import cv2 as cv

img = cv.imread("Images\Ball.jpg",1)
font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img,"Hello world",(0,128),font,2.5,(255,0,0),5,cv.LINE_AA)

cv.imshow("Rectangle",img)
cv.waitKey(0)
cv.destroyAllWindows()