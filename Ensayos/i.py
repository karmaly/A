import numpy as np

# Crear un array de ejemplo con una forma desconocida
array = np.random.randint(1, 10, size=(3, 4, 5))  # Por ejemplo, una matriz 3D de forma desconocida

# Elegir el eje a lo largo del cual calcular el logaritmo
eje = 2  # Por ejemplo, calcular el logaritmo a lo largo del segundo eje

# Obtener la forma actual del array
shape = array.shape

# Intercambiar los ejes para que el eje especificado esté en el primer lugar
array_swapped = np.swapaxes(array, 0, eje)

# Calcular el logaritmo
log_array_along_axis = np.log(array_swapped, where=(array_swapped > 0))

# Revertir los ejes a la forma original
log_array_along_axis = np.swapaxes(log_array_along_axis, 0, eje)

# Mostrar resultados
print("Array original:")
print(array)
print("\nLogaritmo a lo largo del eje", eje, ":")
print(log_array_along_axis)