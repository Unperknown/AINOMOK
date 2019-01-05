import cv2
import numpy as np

ESC = 27
lowerWhite = np.array([0,0,195])
upperWhite = np.array([255,75,255])

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
		np.hstack((resultW, resultB))
		result = np.concatenate((resultW, resultB), axis=1)
		cv2.imshow('Result', result)
		
		# close when ESC pressed
		c = cv2.waitKey(10)
		if c == ESC:
			break
	cv2.destroyAllWindows()

