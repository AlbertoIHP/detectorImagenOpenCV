import cv2
import numpy as np

# 500 x 250
#Se leen las imagenes
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

#Se suman las imagenes (DEBEN TENER LA MISMA RESOLUCION)
#add = img1+img2
#add = cv2.add(img1, img2)

#Ponderacion de ambas imagenes
#Primer parametro es la imagen a trabajar
#Segundo parametro es el alpha de esa imagen respectiva a multiplicar
#Tercer parametro la segunda imagen que se desea trabajar
#Cuarto parametro es el beta que la segunda imagen poseera
#Quinto parametro un ultimo valor que se desee agrega a la ponderecion
# De esta manera esta lista la ponderacion (http://docs.opencv.org/3.1.0/d2/de8/group__core__array.html#gafafb2513349db3bcff51f54ee5592a19)
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)


cv2.imshow('add',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()