import numpy as np
import pandas as pd 

while True:
    url = input('Ingrese URL del archivo: ')
    try:
        dic = pd.read_csv(url)
        # print(dic)
        for i in range(len(dic.columns)):
            print(dic.columns[i])
        break
    except FileNotFoundError:
        print("Archivo no hallado")
        continue
