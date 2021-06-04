#### Eye Detection using Haar Cascade Classifier
import cv2 as cv
eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
# cap = cv.VideoCapture("Videos\Eye-Cap-2.mp4")
cap = cv.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    grey_vid = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    eye_detect = eye_cascade.detectMultiScale(grey_vid)
    for (x,y,w,h) in eye_detect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=2)
    cv.imshow("Eye-Detect", frame)
    if (cv.waitKey(1) & 0xFF == ord("e")):
        break
cap.release()
cv.destroyAllWindows()