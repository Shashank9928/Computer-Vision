import cv2 as cv
import datetime as dt

cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_COMPLEX
#### 3 for width  for height of video
# text = "Width : " + str(cap.get(3)) + " Height : " + str(cap.get(4))
text  = str(dt.datetime.now())
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        Frame = cv.putText(frame,text,(0,50),font,1,(255,0,0),2,cv.LINE_AA)
        cv.imshow("Recording video", Frame)

        if (cv.waitKey(1) & 0xFF == ord("e")):
            break