import numpy as np

a = np.zeros((3, 4) , dtype=int)
print(a)

unos = np.ones(4, dtype=int)
mod = a.copy()
print(unos)
mod[0] = unos
print(mod)

b = list(range(5,9))
print(b)
mod1 = a.copy()
mod1[2] = b
print(mod1)

vec = np.arange(start=1, stop=11  , dtype=int)
print(vec)
for i in range(len(vec)):
    if i % 2 == 0:
        vec[i] = 1
for i in range(len(vec)):
    if i % 2 != 0:
        vec[i] = 0
print(vec)

values = np.arange(25)
v1, v2, v3, v4, v5 = np.split(values, [5, 10, 15, 20])
a = [v1, v2, v3, v4, v5]
print(v1, v2, v3, v4, v5)
matriz = np.array(a)
print(matriz)

matriz2 = np.arange(25).reshape(5,5)
print(matriz2)
print(matriz2)

