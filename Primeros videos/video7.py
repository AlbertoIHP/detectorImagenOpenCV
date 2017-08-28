import cv2
import numpy as np

cap = cv2.VideoCapture(0)
try:
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
		
		
		moments = cv2.moments(mask)
		area = moments['m00']
	 
		#raw_input(mask)
		#Descomentar para ver el area por pantalla
		#print area
		if(area > 100000):
			 
			#Buscamos el centro x, y del objeto
			x = int(moments['m10']/moments['m00'])
			y = int(moments['m01']/moments['m00'])
			 
			#Mostramos sus coordenadas por pantalla
			print "x = ", x
			print "y = ", y
	 
			#Dibujamos una marca en el centro del objeto
			cv2.rectangle(frame, (x-10, y-10), (x+10, y+10),(0,0,255), 2)
		 
		 
		
		
		
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break
			
		cv2.imshow('frame', frame)
		cv2.imshow('mask', mask)
		cv2.imshow('res', res)
		
	cv2.destroyAllWindows()
	cap.release()
except Exception as e:
	print str(e)
	
raw_input(">")