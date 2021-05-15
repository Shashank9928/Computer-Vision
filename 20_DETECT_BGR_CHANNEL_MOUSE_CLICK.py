import numpy as np
import cv2 as cv

def check_bgr(event,x,y,flag,pram):
    if(event == cv.EVENT_RBUTTONDOWN):
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv.FONT_HERSHEY_SIMPLEX
        stXY = "("+str(blue) + "," + str(green)+","+ str    (red) +")"
        cv.putText(img,stXY,(x,y),font,1,(255,0,0),2)
        cv.imshow("MOUSE CLICK BGR",img)
img = cv.imread("Images\Ronaldo-Kick.png")
cv.imshow("MOUSE CLICK BGR",img)
cv.setMouseCallback("MOUSE CLICK BGR",check_bgr)
cv.waitKey(0)
cv.destroyAllWindows()