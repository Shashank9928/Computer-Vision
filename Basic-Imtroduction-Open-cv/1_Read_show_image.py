import cv2 as cv
img = cv.imread("images/Ronaldo-1.jpg",-1)
print(img)

cv.imshow("Image",img)
cv.waitKey(delay=0)
cv.destroyAllWindows()