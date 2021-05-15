#### Face Detection using Haar Cascade Classifier
import cv2 as cv
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
# cap = cv.VideoCapture("Videos\Face-Cap-2.mp4")
cap = cv.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    grey_vid = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(grey_vid,1.1,4)
    for (x,y,w,h) in face_detect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=2)
    cv.imshow("Face-Detect", frame  )
    if (cv.waitKey(1) & 0xFF == ord("e")):
        break
cap.release()
cv.destroyAllWindows()