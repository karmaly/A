import pydicom
import matplotlib.pyplot as plt
import cv2
import numpy as np 
import os

def grafica(ima1, ima2):
    plt.figure(figsize=(15,6))
    plt.subplot(1,2,1)
    plt.imshow(ima1, cmap='inferno', vmin=0, vmax=255)
    plt.subplot(1,2,2)
    plt.imshow(ima2, cmap='inferno', vmin=0, vmax=255)
    plt.show()

print('Primer punto\n')
imagen = cv2.imread('Imagen_celula.jpg')
img_gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) #matriz
#binarización 
umb , imagen_binaria = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY) #devuleve imagen_binaria como una matriz
print(np.shape(imagen_binaria)) 
#gradiente para mejor presicion 
kernel = np.ones((5,5),np.uint8)
imagen_gradiente=cv2.morphologyEx(imagen_binaria, cv2.MORPH_GRADIENT, kernel, iterations = 1)
grafica(imagen_binaria, imagen_gradiente)
#etiquetado
elem,mask=cv2.connectedComponents(imagen_gradiente)
print(f'Número de células: {elem}\n')

print('\npunto 2\n')

data = 'archivosDCM/'

archivos_dcm = [archivo for archivo in os.listdir(data) if archivo.endswith('.dcm')]

archivos_dcm.sort()

imagenes_dcm = []

for archivo in archivos_dcm:
    ruta_completa = os.path.join(data, archivo)
    dcm_data = pydicom.dcmread(ruta_completa)
    imagenes_dcm.append(dcm_data.pixel_array)

for imagen in imagenes_dcm:
    cv2.imshow(f'IMAGEN DICOM', imagen)
    cv2.waitKey(500) #que tan rápido hay que pasar las imágenes? a esta velocidad se ve el cambio constante
    #o debería pasarse manualmente?