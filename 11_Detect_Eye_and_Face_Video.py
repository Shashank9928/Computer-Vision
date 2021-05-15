import cv2 as cv
eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv.VideoCapture("Videos\Eye-Cap-2.mp4")
# cap = cv.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    grey_vid = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    eye_detect = eye_cascade.detectMultiScale(grey_vid)
    face_detect = face_cascade.detectMultiScale(grey_vid,1.1,4)
    for (ex,ey,ew,eh) in eye_detect:
        
        for (fx,fy,fw,fh) in face_detect:
            cv.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),thickness=2)
            cv.rectangle(frame,(fx,fy),(fx+fw,fy+fh),(255,0,0),thickness=2)
    cv.imshow("Eye-Detect", frame)
    if (cv.waitKey(1) & 0xFF == ord("e")):
        break
cap.release()
cv.destroyAllWindows()