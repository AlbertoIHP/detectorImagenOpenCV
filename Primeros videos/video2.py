import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#Se carga un codec
#Depende de las librerias de codec que esten instalados para funcionar
#codec = cv2.cv.FOURCC('M','J','P','G')
#print codec

#Se guarda el video capturado en un archivo de salida
#como primer parametro el nombre de salida
#como segundo el codec
#como tercero el frame rate 
#como cuarto la resolucion

#Con -1 se abre una ventana que da a elegir el codec a usar
outfile = cv2.VideoWriter('output.avi', -1, 20.0,  (640, 480))

while True:
	ret, frame = cap.read()
	
	#Modificamos el frame capturado por la camara, primer parametro el frame
	# Segundo parametro la modificacion deseada
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	#Escribimos cada frame en el archivo de salida
	outfile.write(frame)
	
	#Se muestra en otra ventana
	cv2.imshow('gray', gray)
	
	#Se muestra por ventana el frame capturado por la camara 
	cv2.imshow('frame',frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

print "Liberando recursos"
#Se liberan los recursos y cierran ventanas
outfile.release()
cap.release()
cv2.destroyAllWindows()
raw_input(">Presione para finalizar")