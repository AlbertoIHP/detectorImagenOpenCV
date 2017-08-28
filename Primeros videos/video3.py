import cv2
import numpy as np

img = cv2.imread('watch5050.jpg', cv2.IMREAD_COLOR)

#Dibujamos una linea 
#Primer parametro imagen donde se dibujara
#Segundo parametro donde comienza
#Tercer parametro donde termina
#Cuarto parametro el color
#Quinto parametro numero de pixeles (grosor)
#cv2.line(img,(0,0), (150, 150), (122,122,122), 3)

#Dibujar un rectangulo

#cv2.rectangle(img, (2,2), (50, 50), (255, 0, 122),5   )

#Dibujar un circulo
#Solo cambia que el tercer parametro es el Radio
#Con -1 en el parametro de grosor se hace un rellenado
#cv2.circle(img, (15,15), 15, (0,255,122), 1)

#Dibujar un poligono a partir de una serie de puntos definidos
#en una matriz de numpy
#puntos = np.array([ [2, 3], [6,12], [12, 15], [15, 20], [20, 28] ], np.int32)
#puntos = puntos.reshape((-1, 1, 2))

#Con polylines se unen estos puntos
#Primer parametro la imagen donde se hara
#Segundo los puntos a unir
#Tercer parametro si queremos que el punto inicial con el final se unan
#Cuarto parametro el color
#Quinto parametro grosor
#cv2.polylines(img, [puntos], True, (0,255,255), 3 )


#Escribir en la imagen
#Se elige una fuente 
font = cv2.FONT_HERSHEY_SIMPLEX

#Se pone el texto en la imagen
#Primer parametro la imagen donde se hara
#Segundo aprametro el texto a escribir
#Tercer paramero donde empieza el texto
#Cuarto parametro la fuente
#Quinto parametro TamaNo
#Sexto parametro color
#Septimo parametro espacio entre las letras
cv2.putText(img, 'Hola', (0,10), font, 0.5, (200,255,122), 2)



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()