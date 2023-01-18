import cv2
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

img = cv2.imread('imagen1.jpg',0)
img = cv2.medianBlur(img, 5)


hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Usar libreria de matplot para mostar las imagenes
plt.subplot(221), plt.imshow(img,'gray')
plt.subplot(222), plt.hist(img.ravel(), 256, [0, 256])

plt.title('Imagen gris')
plt.show()
ret, th1 = cv2.threshold(img,180,200, cv2.THRESH_BINARY)
thresh5 = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO_INV)  # Umbralizacion con operador de tozero inverso
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

cv2.imshow('Seleccion',thresh5)

gs = gridspec.GridSpec(2, 2)  # Creamos un grid de 3x3 con matplotlib
plt.subplot(gs[0, 0]), plt.imshow(img, 'gray')  # Graficamos la imagen
plt.title('Imagen original')  # Damos un titulo a la imagen
plt.subplot(gs[0, 1]), plt.imshow(th1, 'gray')  # operador binario
plt.title('Imagen umbral1')
plt.subplot(gs[1, 0]), plt.imshow(th2, 'gray')  # operador binario inverso
plt.title('Imagen umbral2')
plt.subplot(gs[1, 1]), plt.imshow(th3, 'gray')  # operador truncado
plt.title('Imagen umbral3')
plt.show()  # Se plotean los grafico

# Fuente: Documentacion OpenCV
