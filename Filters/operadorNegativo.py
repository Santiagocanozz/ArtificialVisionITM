import numpy as np
import cv2

# Operador negativo
img = cv2.imread('lena.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape[:2]  # Obtenemos sus dimensiones
imgRes = np.ones((height, width), np.uint8)  # Creamos una imagen nueva
imgRes*255
imgNegative = imgRes - grayImg  # Restamos las imagenes
cv2.imshow('imagen_resultado', np.hstack([grayImg, imgNegative]))  # Mostramos las imagenes
cv2.waitKey(0)
cv2.destroyAllWindows()

# Fuente: Documentacion OpenCV
