import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
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
	
	verde_bajos = np.array([49,50,50])
	verde_altos = np.array([80, 255, 255])
	#Necesitamos saber que pixeles de la imagen estan dentro del rango
	#En nuestro caso pintara de blanco los pixeles verdes y de negro el resto
	mask = cv2.inRange(hsv, verde_bajos, verde_altos)
	
	#Desactivamos aquellos bits que no pertenecen a la mascara
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	#Ones retorna una matriz llena de 1, de las dimensiones y tipo especificado en los parametros, se divide en el total de elementos para obtener un promedio
	kernel = np.ones((20,20), np.float32)/400
	
	#Con filter2D es posible convulsionar una imagen con respecto al promedio
	#del parametro entregado en el kernel, primer parametro la imagen a modificar, el segundo es la profundidad y el tercero el kernel
	smoothed = cv2.filter2D(res, -1, kernel)
	
	
	#Filtro gausiano, primer parametro la imagen a resaltar, segundo el tamaño de la matriz de kernel, y el ultimo parametro es la desviacion estandar.
	blur = cv2.GaussianBlur(res, (15,15), 0)
	
	
	#Filtro de mediana, primer parametro imagen a resaltar y segundo paramero el valor lineal de apertura en la imagen
	median = cv2.medianBlur(res, 15)
	
	#Primer parametro la imagen a resaltar, segundo parametro el diametro a partir del que se busca la vecindad de pixeles, 
	#tercer parametro el valor de pixel que define que aquellos pixeles mas lejanos se mezclan 
	#, ultimo parameroe lvalor de sigmaSpace, que se traduce en que los pixeles mas lejanos se mezcalaran mediante sigma color
	bilateral = cv2.bilateralFilter(res, 15, 75, 75)
	
	cv2.imshow('original', frame)
	cv2.imshow('filtrado', res)
	cv2.imshow('filtrado suavizado', smoothed)
	cv2.imshow('filtrado gaussiano', blur)
	cv2.imshow('filtrado con mediana', median)
	cv2.imshow('filtrado con bilateral', bilateral)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2.destroyAllWindows()
cap.release()
	
	