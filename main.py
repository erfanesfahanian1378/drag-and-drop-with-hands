import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8,maxHands=2)
colorR = 255, 0, 255
cx, cy , w, h = 100, 100 , 200 , 200
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)
        cursor = lmList1[8][:2]
        length, info, img = detector.findDistance(lmList1[8][:2], lmList1[12][:2], img)
        print(length)
        if length < 130:
            if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
                colorR = 0, 255, 0
                cx, cy = cursor
            else:
                colorR = 255, 0, 255
        if len(hands)==2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2["center"]
            handType2 = hand2["type"]
            fingers2 = detector.fingersUp(hand2)
            cursor2 = lmList2[8][:2]
            length2, info2, img2 = detector.findDistance(lmList1[8][:2], lmList1[12][:2], img)
            print(length2)
            if length2 < 130 :
                if cx - w // 2 < cursor2[0] < cx + w // 2 and cy - h // 2 < cursor2[1] < cy + h // 2:
                    colorR = 0, 255, 0
                    cx, cy = cursor
                else:
                    colorR = 255, 0, 255

    cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), colorR,cv2.FILLED)
    cv2.imshow('img', img)
    cv2.waitKey(1)


