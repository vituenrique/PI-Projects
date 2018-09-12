import numpy as np
import math

def Negative(img):

	rows, cols = img.shape

	_returnImg = np.zeros((rows, rows), np.uint8)

	for i in range(rows):
		for j in range(cols):
			_returnImg[i, j] = 255 - img[i, j]

	return _returnImg

def ContrastAdjust(img, c, d):

	rows, cols = img.shape

	_returnImg = np.zeros((rows, rows), np.uint8)

	a = np.amin(img)
	b = np.amax(img)

	for i in range(rows):
		for j in range(cols):
			_returnImg[i, j] = (img[i, j] - a) * ((d - c) / (b - a)) + c

	return _returnImg
				
def GammaCorrection(img, gamma):

	if(gamma < 1):
		return img 

	rows, cols = img.shape

	_returnImg = np.zeros((rows, rows), np.uint8)

	for i in range(rows):
		for j in range(cols):
			_returnImg[i, j] = img[i, j] ** gama

	return _returnImg

def LinearEnhancement(img, G, D):
	
	rows, cols = img.shape

	_returnImg = np.zeros((rows, rows), np.uint8)

	for i in range(rows):
		for j in range(cols):
			_returnImg[i, j] = (G * img[i, j]) + D

	return _returnImg

def LogEnhancement(img):
	
	rows, cols = img.shape

	_returnImg = np.zeros((rows, rows), np.uint8)

	G = 255 / math.log10(255)

	for i in range(rows):
		for j in range(cols):
			_returnImg[i, j] = G * math.log10(img[i, j] + 1)

	return _returnImg

def QuadEnhancement(img):

	rows, cols = img.shape

	_returnImg = np.zeros((rows, rows), np.uint8)

	G = 1 / 255

	for i in range(rows):
		for j in range(cols):
			_returnImg[i, j] = G * (img[i, j] ** 2)

	return _returnImg

def SqrtEnhancement(img):

	rows, cols = img.shape

	_returnImg = np.zeros((rows, rows), np.uint8)
	
	G = 255 / math.sqrt(255)
	
	for i in range(rows):
		for j in range(cols):
			_returnImg[i, j] = G * math.sqrt(img[i, j])

	return _returnImg
