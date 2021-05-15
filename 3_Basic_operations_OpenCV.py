import cv2 as cv

img = cv.imread("Images\Ronaldo-1.jpg",1)

cv.imshow("Img window",img)


p = cv.waitKey()
#### 27 ASCIIE code of "ESC"
if (p == 27):
    cv.destroyAllWindows()
elif(p == ord("s")):
    cv.imwrite("copy_img.jpg",img)
    cv.destroyAllWindows()