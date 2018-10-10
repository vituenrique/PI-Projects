import numpy as np
import math 

def Sampling(img, n):
	sample = [lin[::n] for lin in img[::n]]
	return np.array(sample)

def UniformQuantizationV1(img, k):

	img = np.float32(img)
	quantized = img.copy()

	rows, cols, channels = img.shape

	for i in range(rows):
		for j in range(cols):
			quantized[i, j] = ((math.pow(2, k) - 1) * np.float32((img[i, j]) - img.min()) / (img.max() - img.min()))
			quantized[i, j] = np.round(quantized[i, j]) * int(256 / math.pow(2, k))

	return quantized

def UniformQuantizationV2(img, k):
	a = np.float32(img)
	bucket = 256 / k
	quantized = (a / (256 / k))
	return np.uint8(quantized) * bucket

def And(img1, img2):

	if img1.shape == img2.shape:
		row, col = img1.shape

		_returnImg = np.zeros((row, col), np.uint8)

		for i in range(row):
			for j in range(col):
				if img1[i, j] == img2[i, j] and img1[i, j] == 255 and img2[i, j] == 255:
					_returnImg[i, j] = 255
			
	return _returnImg

def Or(img1, img2):

	if img1.shape == img2.shape:
		row, col = img1.shape

		_returnImg = np.zeros((row, col), np.uint8)

		for i in range(row):
			for j in range(col):
				if img1[i, j] == img2[i, j] and img1[i, j] == 0 and img2[i, j] == 0:
					_returnImg[i, j] = 0
				else:
					_returnImg[i, j] = 255
			
	return _returnImg

def Xor(img1, img2):

	if img1.shape == img2.shape:
		row, col = img1.shape

		_returnImg = np.zeros((row, col), np.uint8)

		for i in range(row):
			for j in range(col):
				if img1[i, j] == img2[i, j]:
					_returnImg[i, j] = 0
				else:
					_returnImg[i, j] = 255
			
	return _returnImg

def Not(img1):

	row, col = img1.shape

	_returnImg = np.zeros((row, col), np.uint8)

	for i in range(row):
		for j in range(col):
			if img1[i, j]==255:
				_returnImg[i, j] = 0
			else:
				_returnImg[i, j] = 255
			
	return _returnImg

def Add(img1, img2):

	if img1.shape == img2.shape:
		row, col, channels = img1.shape

		_returnImg = np.zeros((row, col, channels), np.uint8)

		for i in range(row):
			for j in range(col):
				b = (int(img1[i, j, 0]) + int(img2[i, j, 0]))/2
				g = (int(img1[i, j, 1]) + int(img2[i, j, 1]))/2
				r = (int(img1[i, j, 2]) + int(img2[i, j, 2]))/2
				if(b > 255): b = 255
				if(g > 255): g = 255
				if(r > 255): r = 255

				_returnImg[i, j] = [b, g, r]
	return _returnImg

def Sub(img1, img2):

	if img1.shape == img2.shape:
		row, col, channels = img1.shape
		
		_returnImg = np.zeros((row, col, channels), np.uint8)

		for i in range(row):
			for j in range(col):
				b = (int(img1[i, j, 0]) - int(img2[i, j, 0]))/2
				g = (int(img1[i, j, 1]) - int(img2[i, j, 1]))/2
				r = (int(img1[i, j, 2]) - int(img2[i, j, 2]))/2
				if(b < 0): b = 0
				if(g < 0): g = 0
				if(r < 0): r = 0

				_returnImg[i, j] = [b, g, r]
	return _returnImg

def Multi(img, scale):

	row, col, channels = img.shape
		
	_returnImg = np.zeros((row, col, channels), np.uint8)

	for i in range(row):
		for j in range(col):
			b = (img[i, j, 0] * scale)
			g = (img[i, j, 1] * scale)
			r = (img[i, j, 2] * scale)
			if(b > 255): b = 255
			if(g > 255): g = 255
			if(r > 255): r = 255

			_returnImg[i, j] = [b, g, r]
	return _returnImg

def Div(img1, img2):

	if img1.shape == img2.shape:
		row, col, channels = img1.shape
		
		_returnImg = np.zeros((row, col, channels), np.uint8)

		for i in range(row):
			for j in range(col):
				if img2[i, j, 0] != 0:
					b = (img1[i, j, 0] / img2[i, j, 0])
				else:
					b = 0

				if img2[i, j, 1] != 0:
					g = (img1[i, j, 1] / img2[i, j, 1])
				else:
					g = 0
				
				if img2[i, j, 2] != 0:
					r = (img1[i, j, 2] / img2[i, j, 2])
				else:
					r = 0
				np.uint8([b, g, r])
				_returnImg[i, j] = [b, g, r]
	return _returnImg

def AddWeighted(img1, alpha, img2, beta, gama):

	if img1.shape == img2.shape:
		row, col, channels = img1.shape
		
		_returnImg = np.zeros((row, col, channels), np.uint8)

		for i in range(row):
			for j in range(col):
				b1 = (img1[i, j, 0] * alpha)
				g1 = (img1[i, j, 1] * alpha)
				r1 = (img1[i, j, 2] * alpha)

				b2 = (img2[i, j, 0] * beta)
				g2 = (img2[i, j, 1] * beta)
				r2 = (img2[i, j, 2] * beta)

				br = b1 + b2 + gama
				gr = g1 + g2 + gama
				rr = r1 + r2 + gama

				if(br > 255): br = 255
				if(gr > 255): gr = 255
				if(rr > 255): rr = 255

				_returnImg[i, j] = [br, gr, rr]
	return _returnImg

def EuclideanDistance(x1, y1, x2, y2):
	return math.pow(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2), 0.5)

def TranslatePixel(x, y, tx, ty):

	translationMatrix = np.array([1, 0, tx, 0, 1, ty, 0, 0, 1]).reshape((3, 3))
	pixelMatrix = np.array([x, y, 1]).reshape((3, 1))

	translatedMatrix = np.dot(translationMatrix, pixelMatrix)

	return translatedMatrix[0, 0], translatedMatrix[1, 0]

def ScalePixel(x, y, sx, sy):

	scalingMatrix = np.array([sx, 0, 0, 0, sy, 0, 0, 0, 1]).reshape((3, 3))
	pixelMatrix = np.array([x, y, 1]).reshape((3, 1))

	scaledMatrix = np.dot(scalingMatrix, pixelMatrix)

	return scaledMatrix[0, 0], scaledMatrix[1, 0]

def RotatePixel(x, y, angle):

	rotationMatrix = np.array([math.cos(math.radians(angle)), -1 * math.sin(math.radians(angle)), 0, math.sin(math.radians(angle)), math.cos(math.radians(angle)), 0, 0, 0, 1]).reshape((3, 3))
	pixelMatrix = np.array([x, y, 1]).reshape((3, 1))

	rotatedMatrix = np.dot(rotationMatrix, pixelMatrix)

	return rotatedMatrix[0, 0], rotatedMatrix[1, 0]

def Translate(img, tx, ty):

	rows, cols, channels = img.shape

	translatedImage = np.zeros((rows, cols, channels), np.uint8)
	
	for i in range(rows):
		for j in range(cols):

			x, y = TranslatePixel(i, j, ty, tx)

			if x < rows - 1 and y < cols - 1 and x >= 0 and y >= 0:
				translatedImage[x, y] = img[i, j]

	return translatedImage

def Scale(img, sx, sy):
	
	rows, cols, channels = img.shape
	
	scaledImage = np.zeros((rows * math.ceil(sx), cols * math.ceil(sy), channels), np.uint8)

	for i in range(rows):
		for j in range(cols):

			x, y = ScalePixel(i, j, math.ceil(sx), math.ceil(sy))

			scaledImage[x, y] = img[i, j]

	return scaledImage

def Rotate(img, angle, tx = 0, ty = 0):

	rows, cols, channels = img.shape
	rotatedImage = np.zeros((rows, cols, channels), np.uint8)

	for i in range(rows):
		for j in range(cols):
			x, y = TranslatePixel(i, j, -ty, -tx)
			x, y = RotatePixel(x, y, angle)
			x, y = TranslatePixel(x, y, ty, tx)

			if x < rows - 1 and y < cols - 1 and x >= 0 and y >= 0:
				rotatedImage[int(x), int(y)] = img[i, j]

	return rotatedImage
