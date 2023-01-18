import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar imagen
grayImg = cv2.imread('lena.jpg', 0)
equ = cv2.equalizeHist(grayImg)
cv2.imshow('imagen_resultado', np.hstack([grayImg, equ]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas}
hist =  ([grayImg], [0], None, [256], [0, 256])
equHist = cv2.calcHist([equ], [0], None, [256], [0, 256])
# Usar libreria de matplot para mostar las imagenes
plt.subplot(221), plt.hist(grayImg.ravel(), 256, [0, 256])
plt.title('Histograma para imagen gris')
plt.subplot(222), plt.hist(equ.ravel(), 256, [0, 256])
plt.title('Histograma equalizado')
plt.show()

# Fuente: Documentación OpenCV
