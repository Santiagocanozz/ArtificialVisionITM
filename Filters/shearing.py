import numpy as np
import cv2

img1 = cv2.imread('lena.jpg', 0)  # Leemos la imagen
height, width = img1.shape[:2]  # Obtenemos sus dimensiones
img2 = np.zeros((height*2, width*2), np.uint8)  # Creamos una imagen nueva
transMat = np.array([[1, 0, 100], [0, 1, 100], [0, 0, 1]])  # Creamos la matriz de transformacion

for i in range(0, height):
    for j in range(0, width):
        pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
        translation = np.dot(transMat, pos)  # Realizamos el producto punto entre las martices
        img2[translation[0], translation[1]] = img1[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen

cv2.imshow('resultado', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = np.zeros((height*3, width*2), np.uint8)  # Creamos una imagen nueva
transMat3 = np.array([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])  # Creamos la matriz de transformacion

for i in range(0, height*2):
    for j in range(0, width*2):
        pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
        translation = np.dot(transMat3, pos)  # Realizamos el producto punto entre las martices
        img3[int(translation[0]), int(translation[1])] = img2[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen

cv2.imshow('resultado', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Fuente: Documentacion OpenCV
