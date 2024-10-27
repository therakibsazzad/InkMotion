import cv2
import numpy as np
import time
import os
from cvzone.HandTrackingModule import HandDetector
import cvzone

#######################
brushThickness = 10
eraserThickness = 100
########################

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))
header = overlayList[4]
drawColor = (0, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.65, maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    # 1. Import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img, draw=False)

    if lmList:
        # tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()

        # 4. If Selection Mode - Two finger are up
        if fingers[1] and fingers[2]:
            xp, yp = 0,0
            print("Selection Mode")
            # Checking for the click
            if y1 < 130:
                if 25 < x1 < 275:
                    header = overlayList[4]
                    drawColor = (0, 0, 255)
                elif 280 < x1 < 525:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 530 < x1 < 775:
                    header = overlayList[3]
                    drawColor = (150, 0, 190)
                elif 780 < x1 < 1025:
                    header = overlayList[0]
                    drawColor = (0, 0, 0)
                elif 1030 < x1 < 1240:
                    header = overlayList[1]
                    drawColor = (255, 255, 255)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        # 5. If Drawing Mode - Index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)

            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp, yp = x1, y1
#trs
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # Setting the header image
    img[0:130, 0:1280] = header

    # cv2.imshow("Image", img)
    cv2.imshow("Canvas", imgCanvas)
    cv2.imshow("Inv", imgInv)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

