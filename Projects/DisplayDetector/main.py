import cv2
import numpy as np
import os

'''
Resultado obtido: 11
'''

def drawBoundingBox(img, contour, color = (0, 0, 0), border = -1):

	perimeter  = cv2.arcLength(contour, True)
	approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)

	if len(approx) == 4:
		x, y, w, h = cv2.boundingRect(contour)
		cv2.rectangle(img, (x, y), (x + w, y + h), color, border)

def autoCanny(img, sigma = 0.33):

	median = np.median(img)
 
	t1 = int(max(0, (1.0 - sigma) * median))
	t2 = int(min(255, (1.0 + sigma) * median))
	canny = cv2.Canny(img, t1, t2)
 
	return canny

def detectDisplay(filesName = None):

	if filesName != None:

		for i in range(len(filesName)):
			if i % 2 != 1:
				img = cv2.imread("Medidores/" + filesName[i])

				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	
				
				gaussian = cv2.GaussianBlur(gray, (5, 5), 0)

				edges = autoCanny(gaussian, 0.8)
				
				im2, contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

				contours = sorted(contours, key=cv2.contourArea, reverse=True)

				blank = img.copy()

				displayArea = 400

				for c in contours:
					
					area = cv2.contourArea(c)

					if area > displayArea:
						drawBoundingBox(blank, c, (255, 0 , 0), 2)

				cv2.imshow('Detection - ' + filesName[i], blank)
				cv2.waitKey(0)
	else:
		print("Não há imagens para detecção.")

def main():

	files = os.listdir("Medidores")

	detectDisplay(files)
	

if __name__ == "__main__":
	main()