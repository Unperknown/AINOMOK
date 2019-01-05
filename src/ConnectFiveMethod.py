import numpy as np
import cv2

# will be deleted soon
import random

ROW = 19
COLUMN = 19

# will be modified soon
def detectDifferencePosition():
	return random.randint(0, ROW - 1), random.randint(0, COLUMN - 1)

def getPositionFromAI():
	return random.randint(0, ROW - 1), random.randint(0, COLUMN - 1)
