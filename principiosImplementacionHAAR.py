import cv2
import numpy as np

#Leemos la imagen
img = cv2.imread("0003_0007_0017_0049_0049.jpg")

#Se redimensiona (primer principio de implementacion HAAR)
#resized_image = cv2.resize(img, (25,25))

#Se normalizan los valores de intensidad (Imagen - mediaImagen)/DesviacionEstandarImagen
print "Restando "+str(np.median(img))
media = np.median(img)
normalizedImg = np.subtract(img, media)
print "Dividiendo por "+str(np.std(img))
desviacionE = np.std(img)
normalizedImg = np.divide(normalizedImg, desviacionE) 

cv2.imwrite("watch5050_Normalizada.jpg", normalizedImg)
raw_input("Presione para continuar...")