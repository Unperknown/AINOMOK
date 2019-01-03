import cv2
import numpy as np

sensitivity = 70
ESC = 27
lowerWhite = np.array([0,0,255 - sensitivity])
upperWhite = np.array([255,sensitivity,255])

lowerBlack = np.array([0,0,0])
upperBlack = np.array([360,360,115])

if __name__ == '__main__':
	capture = cv2.VideoCapture(1)
	while capture.isOpened():
		_, frame = capture.read()
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		maskW = cv2.inRange(hsv, lowerWhite, upperWhite)
		resultW = cv2.bitwise_and(hsv, hsv, mask=maskW)
		maskB = cv2.inRange(hsv, lowerBlack, upperBlack)
		resultB = cv2.bitwise_and(hsv, hsv, mask=maskB)
		cv2.imshow('Before', frame)
		np.hstack((resultW, resultB))
		result = np.concatenate((resultW, resultB), axis=1)
		cv2.imshow('Result', result)
		c = cv2.waitKey(10)
		if c == ESC:
			break

	cv2.destroyAllWindows()
