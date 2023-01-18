import numpy as np
import cv2

# Operador negativo
img = cv2.imread('lena.jpg')
height, width = img.shape[:2]  # Obtenemos sus dimensiones
print(height, '|', width)
imgGamma = np.zeros((height, width, 3), np.uint8)  # Creamos una imagen nueva
invGamma = 1/0.5  # Se define el valor de Gamma

for i in range(0, height):
    for j in range(0, width):
        imgGamma[i,j] = 255*((img[i, j]/255.0)**invGamma)  # Ecucacion de correccion Gamma

cv2.imshow('correccion_gamma', np.hstack([img, imgGamma]))  # Mostramos las imagenes
cv2.waitKey(0)
cv2.destroyAllWindows()

# Fuente: Documentacion OpenCV
