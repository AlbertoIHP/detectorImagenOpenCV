import cv2
import numpy as np

#Se carga el clasificador creado
watch_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#Se inicializa la captura de la imagen por el dispositivo 0 (si se tienen mas camaras utilizar la deseada 1 ,2 ,3 etc...)
cap = cv2.VideoCapture(0)
while True:
	#Se leen los datos capturados por la camara
	ret, img = cap.read()
	
	#Se trabaja en escala de grises 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	#Se aplica la deteccion del clasificador
	watches = watch_cascade.detectMultiScale(gray, 50, 50)
	
	
	for (x,y,w,h) in watches:
		
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 3)
		#Para cada reloj encontrado en la imagen img se le escribe "Watch" con la fuente establecida y los colores dados
		#font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(img,'Watch',(x-w,y-h), font, 0.5, (11,255,255), 2)
		
	#Se visualiza en una ventana la imagen captada y procesada por opencv
	cv2.imshow('img', img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
		
#Se cierran las ventanas y la conexion a la camara
cap.release()
cv2.destroyAllWindows()
	