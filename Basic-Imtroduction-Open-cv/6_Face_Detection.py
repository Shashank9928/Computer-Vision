#### Face Detection using Haar Cascade Classifier
import cv2 as cv
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv.imread("Images\Team-ManU.jpg")
grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face_detect = face_cascade.detectMultiScale(grey_img,1.1,4)

print(face_detect)
for (x,y,w,h) in face_detect:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=2)
cv.imshow("Detect Face",img)
cv.waitKey()