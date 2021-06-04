import cv2 as cv
import time
import mediapipe as mp

class HandDetector():
    def __init__(self,mode=False,maxHands=2,detectioncon=0.5,trackcon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectioncon = detectioncon
        self.trackcon = trackcon

        ### For Hand Capture
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectioncon,self.trackcon)
        ### To daraw the hand land-makrs
        self.mpd = mp.solutions.drawing_utils


    def Find_hands(self,img,draw=True):
        ### Converting image into rgb formet for mediapipe
        rbgimg = cv.cvtColor(img,cv.COLOR_BGR2RGB)

        ### Hand Tracking
        results =  self.hands.process(rbgimg)
        ## Getting land marks if no hand return none
        # print(results.multi_hand_landmarks)
        ### If hand is present in frame
        if results.multi_hand_landmarks:
            #### In case of multiple hands
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpd.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        


def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector = HandDetector()
    while (True):
        success,img = cap.read()
        detector.Find_hands(img=img)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv.putText(img,str(round(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,3,(255,255,255))
        cv.imshow("img",img)
        cv.waitKey(1)

if __name__ == "__main__":
    main()