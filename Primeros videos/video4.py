import cv2
import numpy as np

img = cv2.imread('watch5050.jpg', cv2.IMREAD_COLOR)

#Obtener el color del pixel especifico
pixel = img[22, 22]

#Le cambiamos el color a este pixel
img[22, 22] = [255, 255, 255]

#Obtener toda una region de la imagen
#Muy util para copiar porciones de imagen y pegarlos en otro lado
region = img[10:20, 10:20]

#Transformamos esa region a blanco
img[10:20, 10:20] = [ 255,255,255]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

raw_input(pixel)
raw_input(region)