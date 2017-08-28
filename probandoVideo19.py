
from urllib import urlopen
from urllib import urlretrieve
import cv2
import numpy as np
import os

for file_type in ['neg']:
	print file_type
	raw_input(">Continuar")
	for img in os.listdir(file_type):
		print img
		raw_input(">Continuar")
	#	for ugly in os.listdir('uglies'):
	#		print ugly
	#		raw_input(">Continuar")
