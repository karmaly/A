import numpy as np
import matplotlib as plt
import pandas as pd
import scipy.io as sio

# 1. matríz aleatoria 4D de size 12000000
m4D = np.random.rand(20,20,300,100)
print(m4D.size)

#2. Copia de la matríz anterior pero con 3D
copiam4Da3D = m4D[:,:,:,0].copy()
print(copiam4Da3D.shape)
print(m4D.shape)

#3. Muestra de los atributos de la matríz copiam4D

print(f'''
Los atributos propios de la matríz son:
    Shape (Cantidad de ejes usados): {copiam4Da3D.shape}
    Dim (Dimensión): {copiam4Da3D.ndim}
    Size (Todos los datos que contiene): {copiam4Da3D.size}
    dtype (Tipo de dato que almacena): {copiam4Da3D.dtype}''')

#4. Pasar la matriz copiam4Da3D a 2D:

copiam3Da2D = copiam4Da3D.copy().reshape(400,300)
print(copiam3Da2D.shape)
print(copiam4Da3D.shape)

#5. Función de matríz a dataframe

def NPaDF(a):
    cantf = a.shape[0]+1
    cantc = a.shape[1]+1
    c = pd.DataFrame(a, index = [np.arange(1,cantf)], columns = [np.arange(1,cantc)])
    return c

print(NPaDF(copiam3Da2D))