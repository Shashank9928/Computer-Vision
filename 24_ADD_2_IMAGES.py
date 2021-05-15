import cv2 as cv

img1 = cv.imread("Images/Pitch.jpg")
img2 = cv.imread("Images/Ronaldo-Kick.jpg")

#### Resizing the images to same size
img1 = cv.resize(img1,(600,400))
img2 = cv.resize(img2,(600,400))
#### adding the two images
# output = cv.add(img1,img2)

#### adding using some arguments
output = cv.addWeighted(img1,0.1,img2,1,0)

cv.imshow("Added Images",output)
cv.waitKey(0)
cv.destroyAllWindows()