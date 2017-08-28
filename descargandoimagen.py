from urllib import urlopen
from urllib import urlretrieve
import cv2
import numpy as np
import os


#Con urlretrieve descargamos un enlace definido en el primer parametro, en el lugar definido en el segundo parametro
urlretrieve("http://mms.businesswire.com/media/20150924005395/en/457567/5/EA_logo_Signature.jpg", "logo"+'.jpg')

#Link con todas las URL de distintas imagenes para generar la cascada
neg_images_link= 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
#Abrimos la url, la decodificamos
neg_image_urls = urlopen(neg_images_link).read()#.decode()

print neg_image_urls
print type(neg_image_urls)
raw_input(">Enter para continuar")