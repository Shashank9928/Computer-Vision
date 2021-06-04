import cv2 as cv
import numpy as np


#### To get the event list
# event = [i for i in dir(cv) if "EVENT" in i]
# print(event)

def click_event(event,x,y,flag,pram):
    if(event == cv.EVENT_LBUTTONDOWN):
        # print("(", x , ",", y,")")
        font = cv.FONT_HERSHEY_SIMPLEX
        stXY = "("+str(x) + "," + str(y)+")"
        cv.putText(img,stXY,(x,y),font,1,(0,0,255),2)
        cv.imshow("MOUSE CLICK EVENT",img)
# img = np.zeros([500,500,3],np.uint8)
img = cv.imread("Images\Ball.jpg")
cv.imshow("MOUSE CLICK EVENT",img)
cv.setMouseCallback("MOUSE CLICK EVENT",click_event)
cv.waitKey(0)
cv.destroyAllWindows()