import cv2 as cv

img = cv.imread("Images\All-Balls.jpg")
cv.imshow("Image",img)

### Create a new image
cv.imwrite("copy_all_balls.jpg",img)

cv.waitKey(0)