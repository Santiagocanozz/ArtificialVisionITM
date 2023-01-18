import numpy as np
import cv2

img1 = cv2.imread('gamma.jpg', 0)  # Leemos la imagen
height, width = img1.shape[:2]  # Obtenemos sus dimensiones
img2 = np.zeros((height, width), np.uint8)  # Creamos una imagen nueva
transMat = np.array([[4, 0, 50], [0, 4, 50], [0, 0, 4]])  # Creamos la matriz de transformacion

for i in range(0, height - transMat[0, 2]):
    for j in range(0, width - transMat[1, 2]):
        pos = np.array([[i], [j], [1]])  # Creamos la matriz de posiciones
        translation = np.dot(transMat, pos)  # Realizamos el producto punto entre las martices
       # print(translation)
        img2[translation[0], translation[1]] = img1[i, j]  # Aplicamos las nuevas posiciones para asignar los valores de la imagen

cv2.imshow('resultado', np.hstack([img1, img2]))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Fuente: Documentacion OpenCV
