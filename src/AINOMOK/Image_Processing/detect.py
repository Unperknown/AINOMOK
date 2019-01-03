import cv2
import numpy as np

sensitivity = 70
ESC = 27
lowerWhite = np.array([0,0,185])
upperWhite = np.array([255,70,255])

lowerBlack = np.array([0,0,0])
upperBlack = np.array([360,360,60])

if __name__ == '__main__':
	# loads one video frame from webcam connected with usb port
	capture = cv2.VideoCapture(1)
	# exception when webcam is not working
	while capture.isOpened():
		_, frame = capture.read()
		# detect color
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		maskW = cv2.inRange(hsv, lowerWhite, upperWhite)
		resultW = cv2.bitwise_and(hsv, hsv, mask=maskW)
		maskB = cv2.inRange(hsv, lowerBlack, upperBlack)
		resultB = cv2.bitwise_and(hsv, hsv, mask=maskB)
		# show result & compare with original frame
		cv2.imshow('Before', frame)
		cv2.imshow('White', resultW)
		cv2.imshow('Black', resultB)
		
		# close when ESC pressed
		c = cv2.waitKey(10)
		if c == ESC:
			break
	cv2.destroyAllWindows()
