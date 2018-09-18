import numpy as np
import math

import matplotlib.pyplot as plt

def calcHist(img):

	rows, cols = img.shape

	hist = np.zeros((256), np.uint8)

	for i in range(rows):
		for j in range(cols):
			hist[img[i, j]] = hist[img[i, j]] + 1

	return hist

def calcNormalizedHist(img):

	rows, cols = img.shape

	normalized = np.zeros((256), np.float16)

	n = rows * cols
	hist = calcHist(img)

	for i in range(256):
		normalized[i] = hist[i] / n

	return normalized

def calcCumulativeHist(img):

	rows, cols = img.shape

	cumulative = np.zeros((256), np.uint16)

	hist = calcHist(img)
	
	cumulative[0] = hist[0] 
	for i in range(1, 256):
		cumulative[i] = hist[i]
		cumulative[i] = cumulative[i] + cumulative[i - 1]

	return cumulative

def calcEqualizeHist(img):
	rows, cols = img.shape

	_returnImg = np.zeros((rows, cols), np.uint8)

	hist = calcHist(img)
	cumulative = calcCumulativeHist(img)
	
	factor = (255) / (rows * cols)

	for k in range(256):
		cumulative[k] = round(cumulative[k] * factor)

	for i in range(rows):
		for j in range(cols):
			pixel = img[i, j]

			newPixel = cumulative[pixel]

			_returnImg[i, j] = newPixel

	return _returnImg



def plotHistogram(hists = None):
	if hists != None:
		nHists = len(hists)
		if nHists > 0:
			if nHists == 1:
				plt.plot(hists[0])
			else:
				value = 200 + (math.ceil(nHists/2) * 10) + 1
				for i in range(nHists):
					plt.subplot(value)
					plt.plot(hists[i])
					value = value + 1

			plt.show()
		else:
			print("O numero de histogramas deve esta entre 1.")
	else:
		print("Nenhum parametro foi passado.")