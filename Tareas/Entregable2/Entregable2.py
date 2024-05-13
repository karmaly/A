# Importo fuciones para:

import numpy as np # manejar matrices
import matplotlib.pylab as plt # graficar
from matplotlib.animation import FuncAnimation

import cv2 #manipular imagenes

import os #manipulación de urls

import cv2 #manipular imagenes

import pydicom #manipular archivos .dcm
from pydicom import dcmread

print('\nPunto 1\n')

#Método graficadora con matplotlib. Dado que cv2 tiene su tono 'gris' particular, en la graficadora
#se adopta la escala de grises más común.
def grafica(ima1, ima2, tipo):
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.title('Imagen A')
    plt.imshow(ima1, cmap='gray', vmin=0, vmax=255)
    plt.subplot(1,2,2)
    plt.title(f'Imagen transformada: {tipo}')
    plt.imshow(ima2, cmap='gray', vmin=0, vmax=255)
    plt.show()
 
#Se lee la imagen con cv2
ima=cv2.imread('Tareas\Entregable2\Imagencel.jpg')

#Cambio de espacio de color de BGR a Grises: La imagen adopta un con color 'gris' según su lógica.
#se binariza la imagen tomando como umbral el 50, haciendo a 0 todos los valores por debajo del umbral.
imag=cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)
umbral, imgB=cv2.threshold(imag,50,255,cv2.THRESH_BINARY)
grafica(imag, imgB, 'Escala de grises')

#Transormaciones morfologicas
#Se crea el kernel o filtro a aplicar a la imagen binarizada
kernelc = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))

# Etiquetado. Se hacen las transformaciones morfológicas necesarias para poder realizar el conteo de elemnetos.
imaOp = cv2.morphologyEx(imgB, cv2.MORPH_OPEN, kernelc, iterations = 1)
imaOO = cv2.morphologyEx(imaOp, cv2.MORPH_OPEN, kernelc, iterations = 3)
imaCl = cv2.morphologyEx(imaOO, cv2.MORPH_CLOSE, kernelc, iterations = 1)
imaDil = cv2.dilate(imaCl,kernelc,iterations = 1)
grafica(imaOp, imaDil, 'Conteo')
elem,mask=cv2.connectedComponents(imaDil)
print(f'Se tienen un total de {elem} células.')

print('\nPunto 2\n')

data = 'Tareas/Entregable2/archivosDCM'

archivos_dcm = [archivo for archivo in os.listdir(data) if archivo.endswith('.dcm')]

archivos_dcm.sort()

imagenes_dcm = []

for archivo in archivos_dcm:
    ruta_completa = os.path.join(data, archivo)
    dcm_data = pydicom.dcmread(ruta_completa)
    arreglo = dcm_data.pixel_array
    max_valor = arreglo.max()  # Obtener el valor máximo de la imagen original
    imagen_normalizada = arreglo / max_valor  # Normalizar la imagen
    imagen_normalizada = (imagen_normalizada * 255).astype(np.uint8)  # Escalar y convertir a uint8
    imagenes_dcm.append(imagen_normalizada)

for imagen in imagenes_dcm:
    cv2.imshow(f'IMAGEN DICOM', imagen)
    cv2.waitKey(500) #que tan rápido hay que pasar las imágenes? a esta velocidad se ve el cambio constante
    #o debería pasarse manualmente?