import cv2
import numpy as np

# Load two images
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

# A partir del tamano de la imagen 2 (El logo)
# se genera una region en la imagen 1 (el grafico)
# De esta manera la region es exactamente el tamano de la imagen 2
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]


# Se transforma la imagen a escala de grises
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# Al transformar la imagen a escala de grises se puede generar una mascara
# mediante el metodo threshold que dentro de sus parametros esta
# El primero la imagen que se desea utilizar para generar la mascara
# El segundo es el limite o tresh 
# El tecero es el maximo valor 
# El cuarto es el metodo que se desea utilizar (http://docs.opencv.org/2.4/doc/tutorials/imgproc/threshold/threshold.html)
# El metodo de tresh invertido basicamente busca los valores de la imagen donde un punto es mayor al limite (tresh) y se reemplaza por un valor estandar (constante)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

#Con bitwise not podemos generar una nueva mascara invirtiendo los valores binarios 
# de la mascara anterior, de esta manera se invierten los valores(color)
mask_inv = cv2.bitwise_not(mask)

# Usando el mismo metodo bitwise aquellos puntos que si pertenzcan al area (desactivando aquellos bits que no pertenecen a la mascara)
# o region definida anteriormente se les aplicara la mascara creada anteriormente
# Primer parametro recurso1 o region1
# Segundo parametro recurso 2 o region2
# tercer parametro  matriz de canal unico de 8 bits, que especifica los elementos de la matriz de salida que desea cambiar
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Se toma solo la region de interes
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)


dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('a',img2gray)
cv2.imshow('b',mask)
cv2.imshow('c', mask_inv)
cv2.imshow('d', img1_bg)
cv2.imshow('e', img2_fg)
cv2.imshow('f', dst)
cv2.imshow('g', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()