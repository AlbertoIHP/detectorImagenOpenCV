from urllib import urlopen
from urllib import urlretrieve
import cv2
import numpy as np
import os

#Creamos imagenes positivas a partir de las negativas: opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/positivas.dat -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1927 
#Creamos el vector con las imagenes positivas: opencv_createsamples -info info/positivas.dat -num 1927 -w 20 -h 20 -vec positivas.vec
#opencv_traincascade -data data -vec positivas.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 15 -w 20 -h 20





# Recibe como parametro el numero de imagen en el que se va, y la url que se quiere descargar
def almacenar_imagenes(num, urlimg):
	#Link con todas las URL de distintas imagenes para generar la cascada
	neg_images_link= urlimg
	#Abrimos la url, la decodificamos (Si solo se ejecutara read, esta variable quedaria con formato String y no UTF-8 o unicode)
	neg_image_urls = urlopen(neg_images_link).read().decode()
	
	#Si el directorio neg no existe lo crearemos
	if not os.path.exists('neg'):
		os.makedirs('neg')
	
	#Iniciamos un contador, que servira para irle dando nombre
	# e indice a las imagenes descargadas
	pic_num = num
	
	for i in neg_image_urls.split('\n'):
		try:
			print i
			#Con urlretrieve indicamos como primer parametro la url a descargar
			#y como segundo la salida que tendra, en este caso el nombre de la imagen
			#guardada dentro de la carpeta neg creada anteriormente
			print "Descargando la imagen numero "+str(i)
			urlretrieve(i, "neg/"+str(pic_num)+'.jpg')
			
			print "Leyendo la imagen recientemente descargada"
			#Con imread leemos la imagen guardada anteriormente en escala de grises
			img = cv2.imread("neg/"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
			
			
			#Guardamos la imagen redimenzionada mediante resize de openCV
			print "Redimenzionando su imagen"
			resized_image = cv2.resize(img, (100,100))
			
			#Escribimos en la misma imagen, la imagen redimenzionada
			print "Guardando el resultado"
			cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)
			
			#Aumentamos el contador de imagen
			pic_num+=1
		except Exception as e:
			print str(e)
	return pic_num


def encontrar_feas():

	#Buscamos dentro del directorio neg
	for file_type in ['neg']:
		print file_type
		#Buscamos todas las imagenes que hayan dentro (con listdir se lista todo lo que esta dentro de un directorio pero sabemos que en este caso son solo imagenes)
		for img in os.listdir(file_type):
			#Listamos las imagenes que tengamos dentro de la carpeta uglies que son la referencia de una imagen no funcional (En este caso solo tenemos una)
			for ugly in os.listdir('uglies'):
				try:
					#Grabamos en una variable la direccion de la imagen.
					current_image_path = str(file_type)+'/'+str(img)
					#Guardamos en una variable la imagen que se considera no funcional
					ugly = cv2.imread('uglies/'+str(ugly))
					#Guardamos en una variable la imagen que queremos comparar si es funcional o no
					question = cv2.imread(current_image_path)
					
					#Se compara si es que sus valores numericos son iguales, de ser asi se elimina la imagen que estaba en duda
					if ugly.shape == question.shape and not(np.bitwise_xor(ugly, question).any()):
						
						print "Se eliminara: "+str(current_image_path)
						os.remove(current_image_path)
				except Exception as e:
					print str(e)
	
	
def generarFicherosData():
	for file_type in ['neg']:
		
		for img in os.listdir(file_type):
		
			# Se comprueba que este en el directorio neg
			if file_type == 'neg':
				#Si es asi, entonces se guardara en una variable la direccion de la imagen encontrada
				line = file_type+'/'+img+'\n'
				
				#Con with, abrimos un documento de texto plano en el que grabaremos la linea generada anteriormente
				with open('bg.txt','a') as f:
					f.write(line)
			# Se comprueba que este en el directorio pos
			elif file_type == 'pos':
				#Si es asi, entonces se guardara en una variable la direccion de la imagen encontrada (Recordar que se debe especificar la ubicacion del objeto de interes y su tamano)
				line = file_type+'/'+img+' 1 0 0 50 50\n'
				#Con with, abrimos un documento de texto plano en el que grabaremos la linea generada anteriormente
				with open('info.dat','a') as f:
					f.write(line)
				
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
raw_input(">Presione para comenzar")
	
#numero = 1			
#SE BAJAN 100
#numero = almacenar_imagenes(numero,  'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513')
# SE BAJAN 100 mas, (NUMERO 100)
#numero = almacenar_imagenes(numero, 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152')
#print "Se guardaron "+str(numero)+" imagenes"

encontrar_feas()
#generarFicherosData()
raw_input(">Listo! , presione para finalizar")