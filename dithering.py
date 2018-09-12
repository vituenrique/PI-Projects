import numpy as np
from random import randint
import math

def BasicDithering(img):

	rows, cols = img.shape

	threshold = 255 / 2

	_returnImg = np.zeros((rows, cols), np.uint8)

	for i in range(rows):
		for j in range(cols):
			if(img[i, j] >= threshold):
				_returnImg[i, j] = 255

	return _returnImg

def RandomDithering(img):

	rows, cols = img.shape

	threshold = 255 / 2

	_returnImg = np.zeros((rows, cols), np.uint8)

	for i in range(rows):
		for j in range(cols):
			temp = img[i, j] + randint(-127, 127)
			if(temp >= threshold):
				_returnImg[i, j] = 255

	return _returnImg

def OrderedDitheringWithClusteredDots(img):

	rows, cols = img.shape

	_returnImg = np.zeros((rows, cols), np.uint8)

	dither = np.array([8, 3, 4, 6 , 1 , 2, 7, 5 ,9]).reshape(3, 3)
	maximun = np.amax(img)

	for i in range(rows):
		for j in range(cols):

			m = i % 3
			n = j % 3

			temp1 = img[i, j] / maximun
			temp2 = dither[m, n] / 10 

			if(temp1 > temp2):
				_returnImg[i, j] = 255

	return _returnImg
				
def OrderedDitheringdWithDispersedDots(img):

	rows, cols = img.shape

	_returnImg = np.zeros((rows, cols), np.uint8)

	ditherBayer = np.array([2, 3, 4, 1]).reshape(2, 2)
	maximun = np.amax(img)

	for i in range(rows):
		for j in range(cols):

			m = i % 2
			n = j % 2

			temp1 = img[i, j] / maximun
			temp2 = ditherBayer[m, n] / 5

			if(temp1 > temp2):
				_returnImg[i, j] = 255

	return _returnImg

def DitheringFloydSteinberg(img):

	rows, cols = img.shape

	threshold = 255 / 2

	_returnImg = np.zeros((rows, cols), np.uint8)

	for i in range(rows - 1):
		for j in range(cols - 1):
			if(img[i, j] >= threshold):
				_returnImg[i][j] = 255

			erro = img[i, j] - _returnImg[i, j]
			_returnImg[i + 1, j] = _returnImg[i + 1, j] + erro * (7 / 16)
			_returnImg[i, j + 1] = _returnImg[i, j + 1] + erro * (5 / 16)
			_returnImg[i + 1, j + 1] = _returnImg[i + 1, j + 1] + erro * (1 / 16)
			_returnImg[i - 1, j + 1] = _returnImg[i - 1, j + 1] + erro * (3 / 16)

	return _returnImg