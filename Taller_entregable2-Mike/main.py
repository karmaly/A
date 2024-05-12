import pydicom
import matplotlib.pyplot as plt
import cv2
import numpy as np 
import os



print('\npunto 2\n')

data = 'Entregable2/archivosDCM'

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