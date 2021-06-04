#### Eye and Face Detection using Haar Cascade Classifier
import cv2 as cv
eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv.imread("Images\Ronaldo-1.jpg")
grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
eye_detect = eye_cascade.detectMultiScale(grey_img)
face_detect = face_cascade.detectMultiScale(grey_img,1.1,4)


for (ex,ey,ew,eh) in eye_detect:
    for (fx,fy,fw,fh) in  face_detect:
        cv.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),thickness=2)
        cv.rectangle(img,(fx,fy),(fx+fw,fy+fh),(255,0,0),thickness=2)
cv.imshow("Detect Eye and Face Image",img)
cv.waitKey()