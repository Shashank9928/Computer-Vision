import numpy as np
import cv2 as cv

def draw_line(event,x,y,flag,pram):
    if(event == cv.EVENT_LBUTTONDOWN):
        cv.circle(img,(x,y),10,(0,0,255),1)
        points.append((x,y))
        if (len(points) >= 2):
            cv.line(img,points[-1],points[-2],(255,0,0),1)
        cv.imshow("POINT JOIN",img)
points = []
img = np.zeros([500,500,3],np.uint8)
cv.imshow("POINT JOIN",img)
cv.setMouseCallback("POINT JOIN",draw_line)
cv.waitKey(0)
cv.destroyAllWindows()