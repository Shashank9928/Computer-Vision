import numpy as np
import cv2 as cv

def show_color(event,x,y,flag,pram):
    if(event == cv.EVENT_LBUTTONDOWN):
        B = img[y,x,0]
        G = img[y,x,1]
        R = img[y,x,2]
        img_color = np.zeros([300,300,3],np.uint8)
        img_color[:] = [B,G,R]
        cv.imshow("IMG COLOR",img_color)


img = cv.imread("Images\Color-Balls-2.jpg")
cv.imshow("IMAGE",img)
cv.setMouseCallback("IMAGE",show_color)
cv.waitKey(0)
cv.destroyAllWindows()