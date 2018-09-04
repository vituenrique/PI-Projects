import cv2
from operations import *

def main():
	
	img1 = cv2.imread('Images/teste1.png')
	img2 = cv2.imread('Images/teste2.png')
	img3 = cv2.imread('Images/teste3.png', 0)
	img4 = cv2.imread('Images/teste4.png', 0)

	'''
	sampled = Sampling(img1, 2)
	quantized = UniformQuantizationV2(img1, 200)

	_and = And(img3, img4)
	_or = Or(img3, img4)
	_xor = Xor(img3, img4)
	_not = Not(img3)

	sum = Add(img1, img2)
	sub = Sub(img1, img2)
	multi = Multi(img1, 0.5)
	div = Div(img1, img2)
	sumWeighted = AddWeighted(img1, 0.5, img2, 0.7, 0)
	
	translated = Translate(img1, 50, -50)
	scaled = Scale(img1, 2, 2)
	rotated = Rotate(img1, 30)

	cv2.imshow('Amostragem', sampled)
	cv2.imshow('Quantizacao', quantized)
	
	cv2.imshow('Img3', img3)
	cv2.imshow('Img4', img4)
	cv2.imshow('And', _and)
	cv2.imshow('Or', _or)
	cv2.imshow('Xor', _xor)
	cv2.imshow('Not', _not)

	cv2.imshow('Img1', img1)
	cv2.imshow('Img2', img2)
	cv2.imshow('Soma', sum)
	cv2.imshow('Soma Ponterada', sumWeighted)
	cv2.imshow('Subtracao', sub)
	cv2.imshow('Multiplicacao', multi)
	cv2.imshow('Divisao', div)
	
	cv2.imshow('Escalonamento', scaled)
	cv2.imshow('Rotacao', rotated)
	cv2.imshow('Translacao', translated)


	'''

	rotated = Rotate(img1, 90, 200, 200)
	cv2.imshow('Rotacao', rotated)

	cv2.waitKey(0)

if __name__ == "__main__":
	main()