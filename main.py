import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, landmark, in enumerate(handLms.landmark):
                #print(id,landmark)
                h,w,c= img.shape
                cx,cy = int(landmark.x*w), int(landmark.y*h)
                print(id,cx,cy)
                if id ==0:
                    cv2.circle(img, (cx,cy), 15,(0, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(20,90), cv2.FONT_HERSHEY_SIMPLEX,3,
                 	(62,58,58))

    cv2.imshow("Camera", img)
    cv2.waitKey(1)