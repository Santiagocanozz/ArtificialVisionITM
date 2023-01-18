import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

# Translacion
img = cv2.imread('luna.jpg', 0)
rows, cols = img.shape
translation = np.float32([[1, 0, 25], [0, 1, 25]])
dst = cv2.warpAffine(img, translation, (cols, rows))
cv2.imshow('Translacion', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Escalado
img11=cv2.imread('t.jpg')
scaling1 = cv2.resize(img11, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Interpolacion Bicubica',scaling1)

img12=cv2.imread('t.jpg')
scaling2 = cv2.resize(img12, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Interpolacion Lineal',scaling2)

img13=cv2.imread('t.jpg')
scaling3 = cv2.resize(img13, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_NEAREST)
cv2.imshow('Interpolacion Nearest',scaling3)

img14=cv2.imread('t.jpg')
scaling4 = cv2.resize(img14, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow('Interpolacion LANCZOS4',scaling4)

img1=cv2.imread('elef.jpg')
scaling1 = cv2.resize(img1, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)
plt.subplot(221), plt.imshow(scaling1)
plt.title('Interpolacion Bicubica')

scaling2 = cv2.resize(img1, None, fx=10, fy=10, interpolation=cv2.INTER_LINEAR)
plt.subplot(222), plt.imshow(scaling2)
plt.title('Interpolacion Lineal ')

scaling3 = cv2.resize(img1, None, fx=10, fy=10, interpolation=cv2.INTER_NEAREST)
plt.subplot(223), plt.imshow(scaling3)
plt.title('Interpolacion Nearest')

scaling4 = cv2.resize(img1, None, fx=10, fy=10, interpolation=cv2.INTER_LANCZOS4)
plt.subplot(224), plt.imshow(scaling4)
plt.title('Interpolacion LANCZOS4')
plt.show()

# Rotacion

height, width = img.shape[:2]
rotation = cv2.getRotationMatrix2D((cols/2, rows/2), 245, 1)
dst = cv2.warpAffine(img, rotation, (cols, rows))
cv2.imshow('Rotacion', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Shearing
transM = np.float32([[1, -math.tan(0.17), 0], [0, 1, 0]])
dst = cv2.warpAffine(img, transM, (cols, rows), cv2.INTER_LINEAR, cv2.BORDER_CONSTANT)
cv2.imshow('Shearing', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Transformacion afine

img = cv2.imread('luna.jpg')
rows, cols, ch = img.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
afineTrans = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, afineTrans, (cols, rows))
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

# Fuente: Documentacion OpenCV
