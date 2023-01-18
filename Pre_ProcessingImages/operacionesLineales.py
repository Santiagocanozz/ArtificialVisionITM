import numpy as np
import cv2

# Copia de imagen
img = cv2.imread('lena.jpg')
height, width = img.shape[:2]  # Obtenemos sus dimensiones
imgCp = np.zeros((height, width, 3), np.uint8)  # Creamos una imagen nueva
# Seccion a color
for i in range(0, height):
    for j in range(0, width):
        imgCp[i, j] = img[i, j]
cv2.imshow('imagen_resultado', np.hstack([img, imgCp]))
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

# Operador suma
img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('lena.jpg')
add = cv2.addWeighted(img1, 1, img2, 1, 0)  # Operador de suma
cv2.imshow('suma', np.hstack([img1, img2, add]))  # Mostramos las imagenes
cv2.waitKey(0)
cv2.destroyAllWindows()

# Operador resta
img3 = cv2.imread('lena.jpg')
img4 = cv2.imread('lena.jpg')
img5=img3-img4
cv2.imshow('i',img5)
subs = cv2.subtract(img3, img4)  # Operador de resta
img3Rs = cv2.resize(img3, (0, 0), fx=0.5, fy=0.5)  # Redimensionamiento
img4Rs = cv2.resize(img4, (0, 0), fx=0.5, fy=0.5)  # Redimensionamiento
subsRs = cv2.resize(subs, (0, 0), fx=0.5, fy=0.5)  # Redimensionamiento
cv2.imshow('resta', np.hstack([img3Rs, img4Rs, subsRs]))  # Mostramos las imagenes
cv2.waitKey(0)
cv2.destroyAllWindows()

# Fuente: Documentacion OpenCV
