import numpy as np
import cv2

img = cv2.imread('img.jpg')  # Leemos la imagen
nSize = 1
height, width = img.shape[:2]  # Obtenemos sus dimensiones
imgGray = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, imgGray)
ret, thr = cv2.threshold(imgGray, 160, 255, cv2.THRESH_BINARY)
cv2.imshow('Thr', thr)
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize=(2*nSize+1, 2*nSize+1), anchor=(-1, -1))

dilate2 = cv2.dilate(thr, element, iterations=1)
cv2.imshow('Dilatacion1',dilate2)# Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas


