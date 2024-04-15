import numpy as np
import matplotlib.pyplot as plt


values = np.arange(25)
v1, v2, v3, v4, v5 = np.split(values, [5, 10, 15, 20])
a = [v1, v2, v3, v4, v5]
print(v1, v2, v3, v4, v5)
matriz = np.array(a)
print(matriz)


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

print(f'{sumaeje(matriz, )} \n')
print(f'{restaeje(matriz, )} \n')
print(f'{diveje(matriz, )} \n')
#print(f'{lognaturaleje(matriz, 0)} \n')
print(f'{promedioeje(matriz, )} \n')
print(f'{desviacionestandareje(matriz, )} \n')