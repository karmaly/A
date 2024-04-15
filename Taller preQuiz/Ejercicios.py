import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io as sio

# 1. Matriz aleatoria 4D de size 12000000
m4D = np.random.rand(20,20,300,100)
print(m4D.size)

#2. Copia de la matriz anterior pero con 3D
copiam4Da3D = m4D.copy()[:,:,:,0]
print(copiam4Da3D.shape)
print(m4D.shape)

#3. Muestra de los atributos de la matriz copiam4D

print(f'''
Los atributos propios de la matriz son:
    Shape (Cantidad de ejes usados): {copiam4Da3D.shape}
    Dim (Dimensión): {copiam4Da3D.ndim}
    Size (Todos los datos que contiene): {copiam4Da3D.size}
    dtype (Tipo de dato que almacena): {copiam4Da3D.dtype}
    nbytes (bytes que ocupa la matriz): {copiam4Da3D.nbytes}
    itemsize (bytes que ocupa cada item o elemento de la matriz): {copiam4Da3D.itemsize}''')
    

#4. Pasar la matriz copiam4Da3D a 2D:

copiam3Da2D = copiam4Da3D.copy().reshape(400,300)
print(copiam3Da2D.shape)
print(copiam4Da3D.shape)

#5. Función de matriz a dataframe

def NPaDF(a):
    cantf = a.shape[0]+1
    cantc = a.shape[1]+1
    c = pd.DataFrame(a, index = [np.arange(1,cantf)], columns = [np.arange(1,cantc)])
    return c

print(NPaDF(copiam3Da2D))

#6. Función que permite cargar un archivo .mat y .csv

def cargaMatoCsV(a):
    if a.endswith("csv"):
        try:
            return pd.read_csv(a)
        except FileNotFoundError:
            return print("Archivo no hallado")
    elif a.endswith("mat"):
        try:
            return sio.loadmat(a)
        except FileNotFoundError:
            return print("Archivo no hallado")
    else:
        return print("No se trata de un archivo .mat o .csv")

print(cargaMatoCsV("Ejercicio.mat"))

# Funciones para operar a lo largo de un eje
# Primer caso: sumar lo largo de un eje
def sumaeje(objeto_nparray, eje):
    a = np.sum(objeto_nparray, axis=eje)
    return a
def restaeje(objeto_nparray, eje):
    a = np.subtract.reduce(objeto_nparray, axis=eje)
    return a
def prodeje(objeto_nparray, eje):
    a = np.prod(objeto_nparray, axis=eje)
    return a
def diveje(objeto_nparray, eje):
    a = np.divide.reduce(objeto_nparray, axis=eje)
    return a
# def lognaturaleje(objeto_nparray, eje):
#     a = np.log(objeto_nparray.copy()[eje], where=(objeto_nparray > 0))
#     b = objeto_nparray[eje] = a
#     return b
def promedioeje(objeto_nparray, eje):
    a = np.mean(objeto_nparray, axis=eje)
    return a
def desviacionestandareje(objeto_nparray, eje):
    a = np.std(objeto_nparray, axis=eje)
    return a


