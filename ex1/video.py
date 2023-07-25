import cv2
import numpy as np


cap =cv2.VideoCapture('video.mp4') #captura a webcam
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

while(True):

    ret, frame = cap.read()
    if ret:
        mask = subtractor.apply(frame)

        kernel = np.ones((5,5), np.uint8)

        mask  = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 1)
        ret, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
        mask = cv2.dilate(mask, kernel, iterations = 2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations = 1)

        contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #contorno primario
        cv2.drawContours(frame, contours, -1, (255, 0 , 0), 1)

        #contorno de selecao
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                cv2.drawContours(frame, cnt, -1, (0, 255, 0), 2)
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 3)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)

        key = cv2.waitKey(30) #delay do video

        if key == ord('q'):
            break


cap.release()


cv2.destroyAllWindows()