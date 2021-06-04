import cv2 as cv
import time
import mediapipe as mp

cap = cv.VideoCapture(0)

### For Hand Capture
mpHands = mp.solutions.hands
hands = mpHands.Hands(False)

### To daraw the hand land-makrs
mpd = mp.solutions.drawing_utils

pTime = 0
cTime = 0
while (True):
    success,img = cap.read()
    ### Converting image into rgb formet for mediapipe
    rbgimg = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    ### Hand Tracking
    results = hands.process(rbgimg)
    ## Getting land marks if no hand return none
    # print(results.multi_hand_landmarks)
    ### If hand is present in frame
    if results.multi_hand_landmarks:
        #### In case of multiple hands
        for handLms in results.multi_hand_landmarks:
            ### Get the informations of landmarks id=id of hand ; lm = landmarks of hand
            for id, lm in enumerate(handLms.landmark):
                print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)

                if id == 0:
                    cv.putText(img,"0",(cx,cy),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
                if id == 1:
                    cv.putText(img,"1",(cx,cy),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
                if id == 2:
                    cv.putText(img,"2",(cx,cy),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
                if id == 3:
                    cv.putText(img,"3",(cx,cy),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
                if id == 4:
                    cv.putText(img,"4",(cx,cy),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
                if id == 5:
                    cv.putText(img,"5",(cx,cy),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
                if id == 6:
                    cv.putText(img,"6",(cx,cy),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
                if id == 7:
                    cv.putText(img,"7",(cx,cy),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
                if id == 8:
                    cv.putText(img,"8",(cx,cy),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))


            ### Draw the landmarks on hands
            mpd.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img,str(round(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,3,(255,255,255))
    cv.imshow("img",img)
    if(cv.waitKey(1) & 0xFF == ord("e")):
        break
cv.destroyAllWindows()