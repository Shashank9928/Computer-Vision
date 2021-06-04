import cv2 as cv
cap = cv.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    #### To change the color 
    grey_vid = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow("Grey-Video",grey_vid)
    if(cv.waitKey(1) & 0xFF == ord("e")):
        break
cap.release()
cv.destroyAllWindows()