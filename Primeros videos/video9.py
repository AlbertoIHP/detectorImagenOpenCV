import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#Obtener codigo rgb en http://html-color-codes.info/codigos-de-colores-hexadecimales/
	
	#Lo metemos en un arreglo de numpy 
	#color_en_rgb  = np.uint8([[[12,22,121]]])
	#Y lo convertimos a la codificacion que opencv le da en hsv
	#color_en_hsv = cv2.cvtColor(color_en_rgb,cv2.COLOR_BGR2HSV)
		
	
	#Necesitamos dos arrays para guardar el rango de colores que 
	#detectamos. El limite inferior sera 49, 50, 50, un verde oscuro.
	#El limite superior sera 80, 255, 255, un verde marino muy claro. 
	#Nuestro programa detectara todos los colores dentro de este rango.
    verde_bajos = np.array([49, 50, 50])
    verde_altos = np.array([80, 255, 255])
	#Necesitamos saber que pixeles de la imagen estan dentro del rango
	#En nuestro caso pintara de blanco los pixeles verdes y de negro el resto
    mask = cv2.inRange(hsv, verde_bajos, verde_altos)
	
	#Desactivamos aquellos bits que no pertenecen a la mascara
    res = cv2.bitwise_and(frame, frame, mask=mask)

	#Construccion de matriz llena de 1
    kernel = np.ones((5, 5), np.uint8)
	
	#Convulsiona una imagen de entrada, en base a un kernel de cualqueir dimension
	#SE usa com oreferencia el punto central del kernel
	#A medida que se analiza la imagen con el kernel, se reemplaza el minimo valor encontrado
	#La erosion hace los objetos negros mas grandes o anchos, y los blancos mas delgados o pequenos
	#Primer parametro la imagen a modificar, segundo el kernel y tecero las iteraciones del kernel sobre la imagen
    erosion = cv2.erode(mask, kernel, iterations=1)
	
	#Convulsiona la imagen de entrada, en base a un kernel de cualqueir dimension
	#Se usa como referencia el punto central del kernel
	#A medida que se analiza con el kernel la imagen original se reemplaza con el valor maximo encontrado
	#La dilatacion hace los objetos negros mas pequenos o delgados, y los blancos mas amplios
	#Primer parametro la imagen a modificar, segundo el kernel y tercero el numero de iteraciones que se recorrera el kernel en la imagen
    dilation = cv2.dilate(mask, kernel, iterations=1)
	
	
	#Es posible combinar los metodos anteriores mediante el metodo morphologyEx
	#Que tendra como variante 2 formas (open y close), el primero realizara una erosion seguida de una dilatacion
	#y el segundo una dilatacion seguida de una erosion.
	#Como primer parametro sera necesario entregar la imagen a modificar, segundo parametro el metodo a utilizar (open o close)
	#ultimo parametro el kernel que recorrera la imagen a analizar
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	
	
    #cv2.imshow('Original', frame)
    #cv2.imshow('Mask', mask)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)
	
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()