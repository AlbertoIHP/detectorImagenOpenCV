import cv2
import numpy as np

try:
	img = cv2.imread('bookpage.jpg')

	
	# Se realiza thresh binary con la imagen a color
	retval, treshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
	
	
	grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#Se realiza thresh binary con la imagen a escala de grises
	retval2, treshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
	
	#A diferencia de los anteriores, este genera un valor thresh para cada seccion
	#de la imagen, de manera que se adecua a las condiciones de cada region de la imagen
	#Con mean se obtiene una media de la zona que se evalua, y con gaussian se realiza una suma ponderada de los valores de la zona
	#Primer parametro la imagen sobre la cual se creara la silueta
	#Segundo parametro el valor maximo
	#Tercer parametro el metodo adaptativo para definir el Tresh
	#Cuarto parametro el metodo de treshold
	#Quinto parametro tamaño del area en pixeles mediante la cual se ira calculando el tresh adaptativo
	#Sexto parametro valor que se resta a la suma ponderada en el caso de utilizar gaussian puede ser 1 y en el caso de usar mean puede ser 0
	gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
	
	
	#Otsu, , se calcula automaticamente el valor thresh a partir del histograma de una imagen bimodal. 
	#(Para las imagenes que no son bimodal, binarizacion no sera exacta.)
	retval2,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	
	cv2.imshow('original', img)
	cv2.imshow('treshold', treshold)
	cv2.imshow('treshold2', treshold2)
	cv2.imshow('gaus', gaus)
	cv2.imshow('otsu', otsu)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
except Exception as e:
	print str(e)

raw_input(">")