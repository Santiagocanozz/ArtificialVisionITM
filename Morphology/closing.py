import numpy as np
import cv2

img = cv2.imread('img.jpg')  # Leemos la imagen
nSize = 1
height, width = img.shape[:2]  # Obtenemos sus dimensiones
imgGray = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, imgGray)
#ret, thr = cv2.threshold(imgGray, 100, 200, cv2.THRESH_BINARY)
kernel = np.zeros((2, 2), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(2*nSize+1, 2*nSize+1))
opening = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=3)
cv2.imshow('Imagen original', img)
cv2.imshow('Apertura', np.hstack([img, opening]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas