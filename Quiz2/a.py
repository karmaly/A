import pandas as pd
import matplotlib.pylab as plt
obj = pd.read_csv(r'Quiz2\brain_stroke 1.csv')

plt.scatter(obj.index, obj['gender'])  # Utiliza los indices como valores para el eje x si tu DataFrame tiene un índice numérico
plt.xlabel('Índice')  # Cambia 'Índice' por el nombre que desees para el eje x
plt.ylabel('Valor de la columna')  # Cambia 'Valor de la columna' por el nombre que desees para el eje y
plt.title('Scatter Plot de una columna')  
plt.grid(True)  # Agrega una cuadrícula al gráfico si lo deseas
plt.show()
