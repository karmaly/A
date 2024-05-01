import numpy as np
import matplotlib.pyplot as ptl
import pandas as pd
import scipy.io as sio

dic = sio.loadmat(r'Quiz2\P005_EP_reposo 1.mat')
cont = 0
catalogo = {}
print('La información contenida en el archivo es la siguiente: ')
for clave, info_ in dic.items(): 
    print(f'''Posición {cont}: El diccionario es "{clave}" y su Clave es:
    {info_}\n''')
    catalogo[cont] = info_
    cont = cont + 1 
