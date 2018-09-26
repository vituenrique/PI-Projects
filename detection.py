import numpy as np
import math 
import cv2

from filters import GaussianFilter
from enhancement import DerivativeX, DerivativeY

# Masks for line detection
maskZero = np.float32((-1, -1, -1, 2, 2, 2, -1, -1, -1))
mask45 = np.float32((-1, -1, 2, -1, 2, -1, 2, -1, -1))
mask90 = np.float32((-1, 2, -1, -1, 2, -1, -1, -2, -1))
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

def BorderDetection(img, threshold = 0):
	# Primeiro passo: Suavizar a imagem (Gaussian)

	_returnImg = GaussianFilter(img)

	# Segundo passo: Ressaltar a imagem (Derivadas parciais em X e Y)

	dx = DerivativeX(_returnImg, [-1, 0, 1])
	dy = DerivativeY(_returnImg, [-1, 0, 1])

	# Terceiro passo: Calcular o modulo do Gradiente

	# Quarto passo: Detectar bordas fortes (Limiarização)

	return [dx, dy]
