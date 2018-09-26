import numpy as np
import math 
import cv2


def IsolatedPoints(img, limiar):
	
	rows, cols = img.shape

	mask = np.float32((-1, -1, -1, -1, 8, -1, -1, -1, -1))

	_returnImg = np.zeros((rows, cols), np.uint8)

	for i in range(1, rows - 1):
		for j in range(1, cols - 1):
			
			value = 0
			neighbors = []

			for x in range(3):
				for y in range(3):
					neighbors.append(img[i - 1 + x, j - 1 + y])

			for k in range(len(neighbors)):
				value += neighbors[k] * mask[k]

			value = math.fabs(value)

			if value > limiar:
				_returnImg[i, j] = 255

	return _returnImg