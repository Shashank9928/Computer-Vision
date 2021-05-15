import cv2 as cv
import matplotlib.pyplot as mlt

img = cv.imread("Images/Gradient.jpg")

_,th0 = cv.threshold(img,50,255,cv.THRESH_BINARY)
_,th1 = cv.threshold(img,50,255,cv.THRESH_BINARY_INV)
_,th2 = cv.threshold(img,50,255,cv.THRESH_TRUNC)
_,th3 = cv.threshold(img,50,255,cv.THRESH_TOZERO)
_,th4 = cv.threshold(img,50,255,cv.THRESH_TOZERO_INV)

titles = ["IMAGE","TH BINARY","TH BINARY INV","TH TRUNC","TH TRUNC INV",
          "TH TOZERO","TH TOZERO INV"]
images = [img,th0,th1,th2,th3,th4]
for i in range(len(images)):
    mlt.subplot(2,3,i+1)
    mlt.imshow(images[i],"gray")
    mlt.title(titles[i])

mlt.show()


