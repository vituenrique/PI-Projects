import numpy as np
import math 
import cv2

def RGB2CMY(img):

	rows, cols, channels = img.shape

	_returnImg = np.zeros((rows, cols, channels), np.uint8)
	
	white = np.array([255, 255, 255])

	for i in range(rows):
		for j in range(cols):			
			_returnImg[i, j] = np.subtract(white, img[i, j])

	return _returnImg

def RGB2YCrCb(img):

	rows, cols, channels = img.shape

	_returnImg = np.zeros((rows, cols, channels), np.uint8)
	
	constY = np.array([0.144, 0.587, 0.299])
	delta = 128

	for i in range(rows):
		for j in range(cols):			
			Y = np.sum(np.multiply(img[i, j], constY))
			Cr = np.sum(np.multiply(np.subtract(img[i, j, 2], Y), 0.713)) + delta
			Cb = np.sum(np.multiply(np.subtract(img[i, j, 0], Y), 0.564)) + delta

			_returnImg[i, j] = [Cb, Cr, Y]
	return _returnImg

def RGB2YUV(img):

	rows, cols, channels = img.shape

	_returnImg = np.zeros((rows, cols, channels), np.uint8)
	
	constY = np.array([0.144, 0.587, 0.299])

	for i in range(rows):
		for j in range(cols):			
			Y = np.sum(np.multiply(img[i, j], constY))
			val = np.subtract(img[i, j, 0], Y)
			U = np.sum(val if val >= 0 else 0)
			val = np.subtract(img[i, j, 2], Y)
			V = np.sum(val if val >= 0 else 0)

			_returnImg[i, j] = [Y, U, V]
	return _returnImg

def RGB2YIQ(img):

	rows, cols, channels = img.shape

	normalized = img.copy()
	normalized = np.divide(normalized, 255)

	_returnImg = np.zeros((rows, cols, channels), np.uint8)
	
	matrix = np.array([0.144, 0.587, 0.299, 
					-0.321, -0.275, 0.596,
					0.311, -0.523, 0.212]).reshape(3, 3)

	for i in range(rows):
		for j in range(cols):			
			YIQ = np.dot(matrix, normalized[i, j])
			YIQ = np.multiply(YIQ, 255)
			_returnImg[i, j] = YIQ
	return _returnImg