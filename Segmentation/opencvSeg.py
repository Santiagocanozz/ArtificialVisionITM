import numpy as np
import cv2
import time

start = time.time()
img = cv2.imread('7.jpg')  # Cargamos la imagen

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
height, width = img.shape[:2]  # Tomamos las dimensiones de la imagen cargada
lower_red = np.array([15, 150,190])  # Creamos un vector con los valores minimos del limite
upper_red = np.array([100, 250, 250])  # Creamos un vector con los valores maximos del limite

mask = cv2.inRange(img, lower_red, upper_red)  # Creamos una mascara con los rangos a segmentar
segImg1 = cv2.bitwise_and(img, img, mask=mask)  # Realimos una operacion bit a bit para aplicar la mascara a la imagen final (conjuncioon logica)
segImg2 = cv2.inRange(img, lower_red, upper_red)  # Segemetacion usando el comando inrange
print(time.time() - start)
cv2.imshow('Color', img)  # Mostramos a imagen original
cv2.imshow('Segmentation1', segImg1)  # Mostramos la imagen segementada
cv2.imshow('Segmentation2', segImg2)  # Mostramos la imagen segementada
cv2.waitKey(0)
cv2.destroyAllWindows()

# Fuente: Documentacion OpenCV
