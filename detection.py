import numpy as np
import math 
import cv2

from filters import GaussianFilter

# Masks for line detection
maskZero = np.float32((-1, -1, -1, 2, 2, 2, -1, -1, -1))
mask45 = np.float32((-1, -1, 2, -1, 2, -1, 2, -1, -1))
mask90 = np.float32((-1, 2, -1, -1, 2, -1, -1, 2, -1))
maskNegative45 = np.float32((2, -1, -1, -1, 2, -1, -1, -1, 2))

def PointDetection(img, threshold = 0):

	if threshold < 0:
		print("O limiar deve ser não negativo!")
		return img
	
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

			if value > threshold:
				_returnImg[i, j] = 255

	return _returnImg

'''
Detecção de Linhas nas seguintes angulações.
	0 - Retas horizontais
	1 - Retas a 45°
	2 - Retas verticais
	3 - Retas a -45°
'''
def LineDetection(img, threshold = 0, mask = 0):
	
	if threshold < 0:
		print("O limiar deve ser não negativo!")
		return img

	if mask == 0:
		mask = maskZero
	elif mask == 1:
		mask = mask45
	elif mask == 2:
		mask = mask90
	elif mask == 3:
		mask = maskNegative45

	rows, cols = img.shape

	_returnImg = np.zeros((rows, cols), np.uint8)

	for i in range(1, rows - 1):
		for j in range(1, cols - 1):
			
			value = 0
			neighbors = []

			for x in range(3):
				for y in range(3):
					neighbors.append(img[i - 1 + x, j - 1 + y])

			for k in range(len(neighbors)):
				value = value + neighbors[k] * mask[k]

			value = math.fabs(value)

			if value > threshold:
				_returnImg[i, j] = 255

	return _returnImg

def DerivativeStandard(img):

	rows, cols = img.shape

	dx = np.zeros((rows, cols), np.uint8)
	dy = np.zeros((rows, cols), np.uint8)

	mask = [-1, 0, 1]

	for i in range(1, rows - 1):
		for j in range(1, cols - 1):
			
			valueX = 0
			valueY = 0
		
			for k in range(3):
				valueX = valueX + img[i - 1 + k, j - 1] * mask[k]
				valueY = valueY + img[i - 1, j - 1 + k] * mask[k]

			valueX = math.fabs(valueX)
			valueY = math.fabs(valueY)

			dx[i, j] = valueX
			dy[i, j] = valueY
	return [dx, dy]

def DerivativeRoberts(img):

	rows, cols = img.shape

	Mx = [1, 0, 0, -1]
	My = [0, -1, 1, 0]

	dx = np.zeros((rows, cols), np.uint8)
	dy = np.zeros((rows, cols), np.uint8)

	for i in range(1, rows - 1):
		for j in range(1, cols - 1):
			
			valueX = 0
			valueY = 0
			
			k = 0
			for x in range(2):
				for y in range(2):
					valueX = valueX + img[i - 1 + x, j - 1 + y] * Mx[k]
					valueY = valueY + img[i - 1 + x, j - 1 + y] * My[k]
					k += 1

			valueX = math.fabs(valueX)
			valueY = math.fabs(valueY)

			dx[i, j] = valueX
			dy[i, j] = valueY
	return [dx, dy]

def DerivativePrewitt(img):

	rows, cols = img.shape

	Gx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
	Gy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

	dx = np.zeros((rows, cols), np.uint8)
	dy = np.zeros((rows, cols), np.uint8)

	for i in range(1, rows - 1):
		for j in range(1, cols - 1):
			
			valueX = 0
			valueY = 0
			
			k = 0
			for x in range(3):
				for y in range(3):
					valueX = valueX + img[i - 1 + x, j - 1 + y] * Gx[k]
					valueY = valueY + img[i - 1 + x, j - 1 + y] * Gy[k]
					k += 1

			valueX = math.fabs(valueX)
			valueY = math.fabs(valueY)

			dx[i, j] = valueX
			dy[i, j] = valueY
	return [dx, dy]

def DerivativeSobel(img):

	rows, cols = img.shape

	Gx = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
	Gy = [-1, -2, -1, 0, 0, 0, 1, 2, 1]

	dx = np.zeros((rows, cols), np.uint8)
	dy = np.zeros((rows, cols), np.uint8)

	for i in range(1, rows - 1):
		for j in range(1, cols - 1):
			
			valueX = 0
			valueY = 0
			
			k = 0
			for x in range(3):
				for y in range(3):
					valueX = valueX + img[i - 1 + x, j - 1 + y] * Gx[k]
					valueY = valueY + img[i - 1 + x, j - 1 + y] * Gy[k]
					k += 1

			valueX = math.fabs(valueX)
			valueY = math.fabs(valueY)

			dx[i, j] = valueX
			dy[i, j] = valueY
	return [dx, dy]

def MagnitudeGradient(Dx, Dy):
	rows, cols = Dx.shape

	magImg = np.zeros((rows, cols), np.uint16)

	for i in range(rows):
		for j in range(cols):
			value = math.fabs(Dx[i, j]) + math.fabs(Dy[i, j])

			magImg[i, j] = value

	return magImg

def Thresholding(img, threshold = 0):
	if threshold < 0:
		print("O limiar deve ser não negativo!")
		return img

	rows, cols = img.shape

	_returnImg = np.zeros((rows, cols), np.uint8)

	for i in range(rows):
		for j in range(cols):
			if img[i, j] > threshold:
				_returnImg[i, j] = 255

	return _returnImg

def BorderDetection(img, threshold = 0, derivative = 0):

	# Primeiro passo: Suavizar a imagem (Gaussian)
	_returnImg = GaussianFilter(img)

	# Segundo passo: Ressaltar a imagem (Derivadas parciais em X e Y)
	if derivative == 0: dx, dy = DerivativeStandard(_returnImg)
	if derivative == 1: dx, dy = DerivativeRoberts(_returnImg)
	if derivative == 2: dx, dy = DerivativePrewitt(_returnImg)
	if derivative == 3: dx, dy = DerivativeSobel(_returnImg)

	# Terceiro passo: Calcular o modulo do Gradiente
	magImg = MagnitudeGradient(dx, dy)

	# Quarto passo: Detectar bordas fortes (Limiarização)
	finalImg = Thresholding(magImg, threshold)

	return finalImg
