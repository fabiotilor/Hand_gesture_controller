import mediapipe as mp
import cv2
import time
import hand_detection as hd
import port_forwarding as pf

open_browser = False #boolean to disallow multiple browser openings
cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0
detector = hd.handDetector()
while True:
     success, img = cap.read()
     img = detector.findHands(img)
     lmList = detector.findPosition(img)
     if len(lmList) != 0:
          print(lmList[12])
          if (lmList[12][2] > lmList[8][2]) and open_browser == False: #Put middle finger down to trigger opening ChatGPT
               pf.open_browser()
               open_browser = True
               #TODO: Add an intuitive way for the user to close the browser and set the boolean back to false (maybe adding a default deactivation and activation gesture)
     cTime = time.time()
     fps = 1 / (cTime - pTime)
     pTime = cTime

     cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 3)
     cv2.imshow("Image", img) 
     cv2.waitKey(1)