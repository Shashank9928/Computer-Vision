#### Eye Detection using Haar Cascade Classifier
import cv2 as cv
eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
img = cv.imread("Images\Ronaldo-1.jpg")
grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
eye_detect = eye_cascade.detectMultiScale(grey_img)

print(eye_detect)
for (x,y,w,h) in eye_detect:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=2)
cv.imshow("Detect Eye",img)
cv.waitKey()