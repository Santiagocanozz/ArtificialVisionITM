import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar imagen
grayImg = cv2.imread('/mnt/Documents/images/lena.jpg', 0)
minVal = np.amin(grayImg)
maxVal = np.amax(grayImg)
hist, bins = np.histogram(grayImg.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()// cdf.max()
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255//(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[grayImg]
plt.subplot(221), plt.imshow(grayImg, 'gray')
plt.title('Imagen gris')
plt.subplot(222), plt.hist(grayImg.ravel(), 256, [0, 256])
plt.title('Histograma para imagen gris')
plt.subplot(223), plt.imshow(img2, 'gray')
plt.subplot(224), plt.hist(img2.ravel(), 256, [0, 256])
plt.show()
