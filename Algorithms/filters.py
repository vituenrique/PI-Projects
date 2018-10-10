import numpy as np
import math

#Low Pass Filters
def MovingAverageFilter(img, window = 3):
	if window % 2 != 1:
		return img

	rows, cols = img.shape

	_returnImg = np.zeros((rows, cols), np.uint8)

	n = int(window / 2)
	
	for i in range(n, rows - n):
		for j in range(n, cols - n):
			value = 0
			for x in range(window):
				for y in range(window):
					value = value + img[i - n + x, j - n + y]

			_returnImg[i, j] = round((value * 1.0) / (window ** 2))

	return _returnImg

def GaussianFilter(img):

	window = 3
	edge = int(window / 2)
	
	rows, cols = img.shape

	mask = np.array((1, 2, 1, 2, 4, 2, 1, 2, 1), np.uint16)

	_returnImg = np.zeros((rows, cols), np.uint8)

	for i in range(edge, rows - edge):
		for j in range(edge, cols - edge):
			
			value = 0
			neighbors = []

			for x in range(window):
				for y in range(window):
					neighbors.append(img[i - edge + x, j - edge + y])

			for k in range(len(neighbors)):
				value = value + neighbors[k] * mask[k]

			newPixel = round(value / 16)

			if newPixel < 0:
				newPixel = 0
			if newPixel > 255:
				newPixel = 255

			_returnImg[i, j] = newPixel

	return _returnImg

def MedianFilter(img, window = 3):

	if window % 2 != 1:
		return img

	edge = int(window / 2)
	
	rows, cols = img.shape

	_returnImg = np.zeros((rows, cols), np.uint8)

	for i in range(edge, rows - edge):
		for j in range(edge, cols - edge):
			
			value = 0
			neighbors = []

			for x in range(window):
				for y in range(window):
					neighbors.append(img[i - edge + x, j - edge + y])

			neighbors.sort()

			_returnImg[i, j] = neighbors[int(len(neighbors) / 2)]

	return _returnImg

