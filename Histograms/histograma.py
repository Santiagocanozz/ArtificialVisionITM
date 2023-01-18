import numpy as np
import cv2  # Se importa la libreria de OpenCV
from matplotlib import pyplot as plt  # Se importa la libreria de Matplot para plotear los histogramas
# Cargar imagen en escala de grises
grayImg = cv2.imread('img.jpg')
# Calcular histograma
hist = cv2.calcHist([grayImg], [0], None, [256], [0, 256])
# Usar libreria de matplot para mostar las imagenes
plt.subplot(221), plt.imshow(grayImg, 'gray')
plt.title('Imagen gris')
plt.subplot(222), plt.hist(grayImg.ravel(), 256, [0, 256])
plt.title('Histograma para imagen gris')
plt.show()

# Fuente: Documentación OpenCV
