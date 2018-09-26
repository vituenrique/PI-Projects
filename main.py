import cv2
from operations import *
from colors import *
from dithering import *
from enhancement import *
from histogram import *
from filters import *
from detection import *

def runOperations():

	img1 = cv2.imread('Images/img1.png')
	img2 = cv2.imread('Images/img2.png')
	img3 = cv2.imread('Images/bin1.png', 0)
	img4 = cv2.imread('Images/bin2.png', 0)

	print("Processando operaçoes...")

	sampled = Sampling(img1, 2)
	quantized = UniformQuantizationV2(img1, 200)

	_and = And(img3, img4)
	_or = Or(img3, img4)
	_xor = Xor(img3, img4)
	_not = Not(img3)

	add = Add(img1, img2)
	sub = Sub(img1, img2)
	multi = Multi(img1, 0.5)
	div = Div(img1, img2)
	sumWeighted = AddWeighted(img1, 0.5, img2, 0.7, 0)
	
	translated = Translate(img1, 50, -50)
	scaled = Scale(img1, 2, 2)
	rotated = Rotate(img1, 30)

	print("Operacoes finalizadas!")

	cv2.imwrite('Outputs/Operations/Img1.png', img1)
	cv2.imwrite('Outputs/Operations/Img2.png', img2)
	cv2.imwrite('Outputs/Operations/Img3.png', img3)
	cv2.imwrite('Outputs/Operations/Img4.png', img4)

	cv2.imwrite('Outputs/Operations/Amostragem.png', sampled)
	cv2.imwrite('Outputs/Operations/Quantizacao.png', quantized)

	cv2.imwrite('Outputs/Operations/And.png', _and)
	cv2.imwrite('Outputs/Operations/Or.png', _or)
	cv2.imwrite('Outputs/Operations/Xor.png', _xor)
	cv2.imwrite('Outputs/Operations/Not.png', _not)

	cv2.imwrite('Outputs/Operations/Soma.png', add)
	cv2.imwrite('Outputs/Operations/Soma Ponterada.png', sumWeighted)
	cv2.imwrite('Outputs/Operations/Subtracao.png', sub)
	cv2.imwrite('Outputs/Operations/Multiplicacao.png', multi)
	cv2.imwrite('Outputs/Operations/Divisao.png', div)
	
	cv2.imwrite('Outputs/Operations/Escalonamento.png', scaled)
	cv2.imwrite('Outputs/Operations/Rotacao.png', rotated)
	cv2.imwrite('Outputs/Operations/Translacao.png', translated)

def runColorModels():

	img = cv2.imread('Images/lenna.png')

	print("Processando conversoes...")

	CMY = RGB2CMY(img)
	YCrCb = RGB2YCrCb(img)
	YUV = RGB2YUV(img)
	YIQ = RGB2YIQ(img)

	print("Conversoes finalizadas!")

	cv2.imwrite('Outputs/ColorModels/YIQ2.png', YIQ)
	cv2.imwrite('Outputs/ColorModels/CMY2.png', CMY)
	cv2.imwrite('Outputs/ColorModels/YUV3.png', YUV)
	cv2.imwrite('Outputs/ColorModels/YCrCb2.png', YCrCb)

def runDithering():

	img = cv2.imread('Images/lenna.png', 0)

	print("Processando Dithering...")

	aleatorio = RandomDithering(img)
	basico = BasicDithering(img)
	aglomeracao = OrderedDitheringWithClusteredDots(img)
	bayer = OrderedDitheringdWithDispersedDots(img)
	floyd = DitheringFloydSteinberg(img)

	print("Dithering finalizados!")

	cv2.imwrite('Outputs/Dithering/aleatorio.png', aleatorio)
	cv2.imwrite('Outputs/Dithering/basico.png', basico)
	cv2.imwrite('Outputs/Dithering/aglomeracao.png', aglomeracao)
	cv2.imwrite('Outputs/Dithering/bayer.png', bayer)
	cv2.imwrite('Outputs/Dithering/floyd.png', floyd)

def runEnhancement():

	img = cv2.imread('Images/lenna.png', 0)

	print("Processando realces...")

	negativo = Negative(img)
	adjust = ContrastAdjust(img, 0, 120)
	gamma = GammaCorrection(img, 0.3)
	linear = LinearEnhancement(img, 1.4, 0)
	log = LogEnhancement(img)
	quad = QuadEnhancement(img)
	sqrt = SqrtEnhancement(img)

	print("Realces finalizados!")

	cv2.imwrite('Outputs/Enhancement/negativo.png', negativo)
	cv2.imwrite('Outputs/Enhancement/ajuste.png', adjust)
	cv2.imwrite('Outputs/Enhancement/gamma.png', gamma)
	cv2.imwrite('Outputs/Enhancement/linear.png', linear)
	cv2.imwrite('Outputs/Enhancement/log.png', log)
	cv2.imwrite('Outputs/Enhancement/quad.png', quad)
	cv2.imwrite('Outputs/Enhancement/sqrt.png', sqrt)

	cv2.imshow('Original', img)
	cv2.waitKey(0)

def runHistogram():

	img = cv2.imread('Images/lenna.png', 0)

	print("Processando histogramas...")

	hist = calcHist(img)
	normalized = calcNormalizedHist(img)

	cumulative = calcCumulativeHist(img)

	streched = calcStrechingHist(img, 8)

	plotHistogram([hist, normalized, cumulative, calcHist(streched)])

	flattened = calcFlattenedHist(img)

	cv2.imshow('Original', img)
	cv2.imshow('Flattened', flattened)
	cv2.imshow('streched', streched)
	cv2.waitKey(0)

	print("Histogramas finalizados!")

def runFilters():
	img = cv2.imread('Images/lenna.png', 0)

	average = MovingAverageFilter(img, 5)
	gaussian = GaussianFilter(img)
	median = MedianFilter(img, 7)

	cv2.imwrite('Outputs/Filters/average.png', average)
	cv2.imwrite('Outputs/Filters/gaussian.png', gaussian)
	cv2.imwrite('Outputs/Filters/median.png', median)

def runDetection():
	img = cv2.imread('Images/solitaria.jpg', 0)

	isolated = IsolatedPoints(img, 254)

	cv2.imwrite('Outputs/Detection/isolated.png', isolated)

def main():
	
	#runOperations()
	#runColorModels()
	#runDithering()
	#runEnhancement()
	#runHistogram()
	#runFilters()
	runDetection()

if __name__ == "__main__":
	main()