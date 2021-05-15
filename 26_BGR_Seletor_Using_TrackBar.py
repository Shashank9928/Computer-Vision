import numpy as np
import cv2 as cv

def display(x):
    print(x)


img = np.zeros([200,250,3],np.uint8)
cv.namedWindow("BGR TrackBar")

### TODO: Creating TrackBar
#### For Blue
cv.createTrackbar("B","BGR TrackBar",0,255,display)
#### For Green
cv.createTrackbar("G","BGR TrackBar",0,255,display)
#### For Red
cv.createTrackbar("R","BGR TrackBar",0,255,display)
cv.createTrackbar("0:OFF \n 1:ON","BGR TrackBar",0,1,display)


while(1):
    cv.imshow("BGR TrackBar",img)
    if (cv.waitKey(1) == 27 & 0xFF):
        break

    B = cv.getTrackbarPos("B","BGR TrackBar")
    G = cv.getTrackbarPos("G","BGR TrackBar")
    R = cv.getTrackbarPos("R","BGR TrackBar")
    s = cv.getTrackbarPos("Switch","BGR TrackBar")
    if s == 0:
        img[:] = 0
    else:
        img[:] = B,G,R

cv.destroyAllWindows()