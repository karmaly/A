# Importo fuciones para:

import numpy as np # manejar matrices
import matplotlib.pylab as plt # graficar

import cv2 #manipular imagenes
import os

import pydicom #manipular archivos .dcm
from pydicom.data import get_testdata_file 
from pydicom import dcmread

import nilearn #Visualización de imágenes en formato NIFTI
from nilearn import plotting 

import dicom2nifti #Conversión DICOM a NIFTI

from PIL import Image #conversión a RGB


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

#Método para hacer transformaciones según el kernel usado y graficarlas
def morfo(imgB, kernel):
    imaEro = cv2.erode(imgB,kernel,iterations = 1) #el pixel central del kernel toma el valor del nivel a dilatar, 
                                                    #si hay alguno de los pixeles al interior del kernel que tengan ese valor.
    imaDil = cv2.dilate(imgB,kernel,iterations = 1) #el pixel central del kernel toma el valor del nivel contrario al del interés, 
                                                    #si hay alguno de lo pixeles al interior del kernel que tengan ese valor.
    imaOp=cv2.morphologyEx(imgB, cv2.MORPH_OPEN, kernel, iterations = 1) #Erosión y luego dilatación ulterior
    imaCl=cv2.morphologyEx(imgB, cv2.MORPH_CLOSE, kernel, iterations = 1) #El cierre es al revés de Apertura, Dilatación seguida de Erosión.
    imaG=cv2.morphologyEx(imgB, cv2.MORPH_GRADIENT, kernel, iterations = 1) #Es la diferencia entre dilatación y erosión de una imagen. El resultado se verá como el contorno del objeto.
    imaTH=cv2.morphologyEx(imgB, cv2.MORPH_TOPHAT, kernel, iterations = 1) #Es la diferencia entre la imagen de entrada y la apertura de la imagen.
    imaBH=cv2.morphologyEx(imgB, cv2.MORPH_BLACKHAT, kernel, iterations = 1) #Es la diferencia entre el cierre de la imagen de entrada y la imagen de entrada
    grafica(imgB,imaEro, 'Erosión')
    grafica(imgB,imaDil, 'Dilatación')
    grafica(imgB,imaOp, 'Apertura') 
    grafica(imgB,imaCl, 'Cierre') 
    grafica(imgB,imaG, 'Gradiente')
    grafica(imgB,imaTH, 'Sombrero de copa') 
    grafica(imgB,imaBH, 'Sombrero negro') 
 
#Se lee la imagen con cv2
ima=cv2.imread('Entregable2\Imagencel.jpg')

#Cambio de espacio de color de BGR a Grises: La imagen adopta un con color 'gris' según su lógica.
#se binariza la imagen tomando como umbral el 50, haciendo a 0 todos los valores por debajo del umbral.
imag=cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)
umbral, imgB=cv2.threshold(imag,50,255,cv2.THRESH_BINARY)
grafica(imag, imgB, 'Escala de grises')

#Transormaciones morfologicas
#Se crean los kernel o filtros a aplicar a la imagen binarizada
kernelr = cv2.getStructuringElement(cv2.MORPH_RECT,(6,6))
kernelc = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
kernele = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))

while True:
    kernel = int(input('Ingrese el kernel a aplicar:\n1. Rectangular\n2. Cruz\n3. Elíptico\n4. Salir\n>  '))
    if kernel == 1:
        morfo(imgB, kernelr)
    elif kernel == 2:
        morfo(imgB, kernelc)
    elif kernel == 3:
        morfo(imgB, kernele)
    elif kernel == 4:
        break
    else:
        print('Elija una de las 3 opciones de kernel.')

# Etiquetado. Se hacen las transformaciones morfológicas necesarias para poder realizar el conteo de elemnetos.
imaOp=cv2.morphologyEx(imgB, cv2.MORPH_OPEN, kernelc, iterations = 1)
imaOO=cv2.morphologyEx(imaOp, cv2.MORPH_OPEN, kernelc, iterations = 3)
imaCl=cv2.morphologyEx(imaOO, cv2.MORPH_CLOSE, kernelc, iterations = 1)
imaDil = cv2.dilate(imaCl,kernelc,iterations = 1)
grafica(imaOp,imaDil, 'Conteo')
elem,mask=cv2.connectedComponents(imaDil)
print(f'Se tinen un total de {elem} células.')

# Guardar la imagen en formato RGB
img_rgb_pil = Image.fromarray(imaDil)
img_rgb_pil.save('./Entregable2/Conteo.jpg')


data = 'Entregable2\archivosDCM'

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