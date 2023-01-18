import numpy as np
import cv2

img1 = cv2.imread('lena.jpg', 0)  # Leemos la imagen
cv2.imshow('d',img1)
height, width = img1.shape[:2]  # Obtenemos sus dimensiones
img2 = np.zeros((height*6, width*6), np.uint8)  # Creamos una imagen nueva
transMat = np.array([[6, 0, 0], [0, 6, 0], [0, 0, 1]])  # Creamos la matriz de transformacion

for i in range(0, height - transMat[0, 2]):
    for j in range(0, width - transMat[1, 2]):
        pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
        translation = np.dot(transMat, pos)  # Realizamos el producto punto entre las martices
        img2[translation[0], translation[1]] = img1[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen

cv2.imshow('resultado', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()