# Importo fuciones para:
import numpy as np # manejar matrices
import matplotlib.pyplot as plt # graficar
import cv2 #manipular imagenes
import scipy.io as sio
import os
import pydicom #manipular archivos .dcm
from pydicom import dcmread
import nilearn #Visualización de imágenes en formato NIFTI
from nilearn import plotting
import nibabel as nib
class Paciente:
    def __init__(self):
        self.__nombre = ''
        self.__cedula = ''
        self.__edad = ''
        self.__lista = []

#Manipulación del atributo tipo lista 
    def agregardicom(self, a):
        self.get_lista().append(a)

#Creación de los atributos del paciente
    def paciente_creado_desde_dicom(self, ruta):
        archivos_dcm = [ archivo for archivo in os.listdir(ruta) if archivo.endswith('.dcm')]
        archivos_dcm.sort()
        for archivo in archivos_dcm:
            ruta_completa = os.path.join(ruta, archivo)
            dcm_data = pydicom.dcmread(ruta_completa)
            self.agregardicom(dcm_data)
            nombre = dcm_data[0x0010 , 0x0010].value
            self.__nombre = nombre
            edad = dcm_data[0x0010 , 0x1010].value
            self.__edad = edad
            cedula = dcm_data[0x0010 , 0x0020].value
            self.__cedula = cedula

#Getters clase Paciente
    def get_Nombre(self):
        return self.__nombre
    def get_Cedula(self):
        return self.__cedula
    def get_Edad(self):
        return self.__edad
    def get_lista(self):
        return self.__lista

#Obtención de arreglos de cada archivo dicom guardado en el paciente.
    def arreglos(self):
        imagenes_dcm = []
        lista = self.get_lista()
        for archivo in lista:
            imagenes_dcm.append(archivo.pixel_array)
        return imagenes_dcm
    
class Graficar_Guardar:
    def __init__(self):
        self.__figura = plt.figure()
        self.__eje1 = self.__figura.add_subplot(1,2,1)
        self.__eje2 = self.__figura.add_subplot(1,2,2) 

    def girada(self, imagen_dicom, angulo, nombrenuevo):
        altura, ancho = imagen_dicom.shape
        centro = (ancho/2, altura/2)
        matriz_rotacion = cv2.getRotationMatrix2D(centro, angulo, 1.0)
        imagen_rotada = cv2.warpAffine(imagen_dicom, matriz_rotacion, (ancho, altura))
        self.__eje1.set_title('Imagen Original')
        self.__eje1.imshow(imagen_dicom, cmap='gray')
        self.__eje2.set_title('Imagen Rotada')
        self.__eje2.imshow(imagen_rotada, cmap='gray')
        max_valor = imagen_rotada.max()  #Obtener el valor máximo de la imagen original
        imagen_normalizada = imagen_rotada / max_valor  # Normalizar la imagen
        cv2.imwrite(nombrenuevo,imagen_normalizada * 255)  # Escalar nuevamente a 0-255 antes de guardar
        print(f'Imagen rotada guardada como "{nombrenuevo}"')
        plt.show()

    def transmorfo(self, ima, A, nombrenuevo):
        umbral, imgB=cv2.threshold(ima,50,255,cv2.THRESH_TOZERO)
        kernelc = cv2.getStructuringElement(cv2.MORPH_CROSS,(A,A))
        imaOp = cv2.morphologyEx(imgB, cv2.MORPH_OPEN, kernelc, iterations = 1)
        texto = f'Imagen binarizada (Umbral: {umbral}, Tamaño del kernel: {A})' 
        max_valor = imaOp.max()  # Obtener el valor máximo de la imagen original
        imagen_normalizada = imaOp / max_valor  # Normalizar la imagen
        imagen_normalizada = (imagen_normalizada * 255).astype(np.uint8)
        texto = f'Imagen binarizada (Umbral: {umbral}, Tamaño del kernel: {A})'
        cv2.putText(imagen_normalizada, texto, (20, imagen_normalizada.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2, cv2.LINE_AA)
        self.__eje1.set_title('Imagen Original')
        self.__eje1.imshow(ima, cmap='gray')
        self.__eje2.set_title('Imagen Transformada')
        self.__eje2.imshow(imagen_normalizada, cmap='gray')
        plt.show()
        cv2.imwrite(nombrenuevo, imagen_normalizada)
        print(f"Imagen transformada guardada como '{nombrenuevo}'")
        plt.show()
        
def ValNumInt(x):
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            return ValNumInt(input('Debe ingresar un dato numérico: '))

def menu_1(dict_pac,dict_arc):
    paciente = Paciente()
    ruta = input('\nIngrese la ruta de la carpeta de los archivos DICOM: ')
    paciente.paciente_creado_desde_dicom(ruta)
    print(f'\nEl nombre del paciente es "{paciente.get_Nombre()}", su iD "{paciente.get_Cedula()}" y su edad de "{paciente.get_Edad()}"')
    clave = paciente.get_Cedula()
    dict_pac[clave] = paciente
    num_ima = len(paciente.get_lista())
    while True:
        imagen = ValNumInt(input(f'\nLa carpeta escogida tiene {num_ima} imágenes. Escoga una de ellas para convertirla nifti: '))
        if 1 <= imagen <= num_ima:
            nombrenuevo = (input(f'\nNombre del nuevo archivo: ')) + '.nii.gz'
            dict_arc[clave] = imagen
            tonifti = paciente.get_lista()[imagen-1].pixel_array
            nifti_image = nib.Nifti1Image(tonifti, affine=None)  # Crear un objeto NIfTI
            nib.save(nifti_image, nombrenuevo)  # Guardar el archivo NIfTI
            break
        else: 
            print(f'Debe escoger un valor entre 1 y {num_ima}')

def menu_2(dict_arc_ima):
    ruta_archivo = input('Ingrese la ruta del archivo: ')
    nombre_archivo = os.path.basename(ruta_archivo)
    imagen = cv2.imread(ruta_archivo)
    dict_arc_ima[nombre_archivo] = imagen
    print(f'La imagen {nombre_archivo} ha sido agregada correctamente al diccionario de archivos.')
       
def menu_3(dict_pac):
    clave = input('\nIngrese el ID del paciente: ')
    if clave in dict_pac:
        pac = dict_pac[clave]
        lista_arreglos = pac.arreglos()
        num_ima = len(lista_arreglos)
        while True:
            imagen = ValNumInt(input(f'\nEl ID escogido tiene {num_ima} imágenes. Escoga una de ellas para rotarla: '))
            if 1 <= imagen <= num_ima:
                original = lista_arreglos[imagen - 1]
                grafica = Graficar_Guardar()
                while True:
                    angulo = ValNumInt(input(f'''\nAngulo a girar:\n1. 90\n2. 180\n3. 270\n> '''))
                    if angulo in [1, 2, 3]:
                        if angulo == 1:
                            angulo = 90
                        elif angulo == 2:
                            angulo = 180
                        else:
                            angulo = 270
                        nombrenuevo = input(f'\nNombre del nuevo archivo: ') + '.png'
                        grafica.girada(original, angulo, nombrenuevo)
                        break
                    else: 
                        print('Debe escoger un valor entre 1 y 3')
                break
            else: 
                print(f'Debe escoger un valor entre 1 y {num_ima}')
    else:
        print('La ID no se halla en la base de datos')       

def menu_4(dict_archivos_ima):
    clave = input('\nIngrese el nombre de la imagen(con la extensión): ')
    if clave in dict_archivos_ima:
        arreglo = dict_archivos_ima[clave]
        arregloB=cv2.cvtColor(arreglo, cv2.COLOR_BGR2GRAY)
        grafica = Graficar_Guardar()
        kernel = ValNumInt(input('Ingrese el tamaño del kernel: '))
        nombrenuevo = (input(f'\nNombre del nuevo archivo: '))+'.png'
        grafica.transmorfo(arregloB, kernel, nombrenuevo)
    else:
        print('La ID no se halla en la base de datos')