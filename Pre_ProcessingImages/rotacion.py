import numpy as np
import cv2
import math

img1 = cv2.imread('lena.jpg', 0)  # Leemos la imagen
height, width = img1.shape[:2]  # Obtenemos sus dimensiones
img2 = np.zeros((height*2, width*2), np.uint8)  # Creamos una imagen nueva
transMat = np.array([[math.cos(np.pi), -math.sin(np.pi), 0], [math.sin(np.pi), math.cos(np.pi), 0], [0, 0, 1]])  # Creamos la matriz de transformacion

for i in range(0, height - int(transMat[0, 2])):
    for j in range(0, width - int(transMat[1, 2])):
        pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
        translation = np.dot(transMat, pos)  # Realizamos el producto punto entre las martices
        img2[int(translation[0]), int(translation[1])] = img1[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen

cv2.imshow('resultado', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Fuente: Documentacion OpenCV
