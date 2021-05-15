import numpy as np
import cv2 as cv

while(True):
    img = cv.imread("Images/Color-Balls-2.jpg")

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower_blue = np.array([0, 51, 0])
    upper_blue = np.array([0, 255, 255])

    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)

    Output_Mask_Bit = cv.bitwise_and(img, img, mask=mask_blue)

    cv.imshow("Image", img)
    cv.imshow("Mask", mask_blue)
    cv.imshow("Output", Output_Mask_Bit)

    key = cv.waitKey()
    if key == 27:
        break

cv.destroyAllWindows()