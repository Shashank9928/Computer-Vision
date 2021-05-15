import cv2 as cv
cap = cv.VideoCapture(0)
print(cap.isOpened())

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
cap.set(3,3000) #### Pid = 3 for width
cap.set(4,2000) #### pid = 4 for height
print(cap.get(3))
print(cap.get(4))
while(True):
    ret,frame = cap.read()
    cv.imshow("Recording video",frame)

    if(cv.waitKey(1) & 0xFF == ord("e")):
        break
cap.release()
cv.destroyAllWindows()