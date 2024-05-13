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

class Paciente:
    def __init__(self):
        self.__nombre = ''
        self.__cedula = ''
        self.__edad = ''
        self.__dicom = []

    def set_dicom(self,d):
        self.__dicom = d
    def agregardicom(self, a):
        self.set_dicom.append(a)

    def paciente_creado_desde_dicom(self, nombredicom):
        data = 'Entregable2/archivosDCM'
        archivos_dcm = [archivo for archivo in os.listdir(nombredicom) if archivo.endswith('.dcm')]
        archivos_dcm.sort()
        for archivo in archivos_dcm:
            ruta_completa = os.path.join(data, archivo)
            dcm_data = pydicom.dcmread(ruta_completa)
            self.agregardicom(dcm_data)
            nombre = dcm_data.PatientName
            self.__nombre = nombre
            cedula = dcm_data.PatientID
            self.__cedula = cedula
            edad = dcm_data.PatientAge
            self.__edad = edad
        
#getter clase paciente
    def get_Nombre(self):
        return self.__nombre
    def get_Cedula(self):
        return self.__cedula
    def get_Edad(self):
        return self.__edad
    def get_dicom(self):
        return self.__dicom

    def arreglos(self):
        imagenes_dcm = []
        lista = self.set_dicom()
        for archivo in lista:
            imagenes_dcm.append(archivo.pixel_array)
        return imagenes_dcm
    
    