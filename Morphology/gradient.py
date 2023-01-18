import numpy as np
import cv2

img = cv2.imread('img.jpg')  # Leemos la imagen
nSize = 7
height, width = img.shape[:2]  # Obtenemos sus dimensiones
imgGray = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, imgGray)
ret, thr = cv2.threshold(imgGray, 200, 255, cv2.THRESH_BINARY_INV)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
gradient = cv2.morphologyEx(thr, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Gradiente', np.hstack([thr, gradient]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas