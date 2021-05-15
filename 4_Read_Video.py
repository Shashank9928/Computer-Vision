import cv2 as cv
#### Video read already exist
# cap = cv.VideoCapture("Videos/1.mp4")
#### Video display from webcam
cap = cv.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    cv.imshow("Recording video",frame)

    if(cv.waitKey(1) & 0xFF == ord("e")):
        break
cap.release()
cv.destroyAllWindows()