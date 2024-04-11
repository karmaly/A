import numpy as np
import matplotlib as plt
import pandas as pt
import scipy.io as sio

# 1. matríz aleatoria 4D de size 12000000
m4D = np.random.rand(20,20,300,100)
print(m4D.size)

#2. Copia de la matríz anterior pero con 3D
copiam4D = m4D[:,:,:,0].copy()
print(copiam4D.shape)
print(m4D.shape)
