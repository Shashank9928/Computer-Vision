import cv2 as cv
import matplotlib.pyplot as mlt

img = cv.imread("Images/Ronaldo-1.jpg",-1)

#### BGR TO RGB FOR MATPLOTLIB

img1 = cv.cvtColor(img,cv.COLOR_BGR2RGB)

mlt.imshow(img1)
mlt.show()

cv.imshow("Image",img)
cv.waitKey(0)
cv.destroyAllWindows()
