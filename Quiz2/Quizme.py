# Importo fuciones para:     
import numpy as np # manejar matrices
import matplotlib.pylab as plt # graficarlas
import pandas as pd # leer(crear) y manipular ciertos archivos (Se convierten en DataFrame)
import scipy.io as sio # y librería para leer archivos .mat

# Clase que almacena por id_ el tipo de dato leído
class sistema: 
    def __init__(self):
        self.__diccsv = {}
        self.__dicmat = {}

    # Se crean métodos propios para la clase

    # Me permite ver los diccionarios creados 
    def verdiccsv(self):
        return self.__diccsv
    def verdicmat(self):
        return self.__dicmat
    
    # Me permite añadir información a los diccionarios creados 
    def agregaracsv(self, id_, dic):
        self.verdiccsv()[id_] = dic
        return print('Asigando con éxito')
    def agregaramat(self, id_, dic):
        self.verdicmat()[id_] = dic
        return print('Asigando con éxito')
    
    # Me permite verificar si el id_ ingresado existe en algúno de los diccionarios propios de la clase. 
    def verificarexistecsv(self, id_):
        if id_ in self.__diccsv:
            return True
        else:
            return False
    def verificarexistemat(self, id_):
        if id_ in self.__dicmat:
            return True
        else:
            return False
      
    # Me permite redimensionar el arreglo y lo retorna para ser usado en la clase graficarmat.
    def dimensionado(self, id_,):
        dim = self.verdicmat()[id_].ndim
        if dim == 2:
            arreglo = self.verdicmat()[id_]
            return arreglo
        else:
            size = self.verdicmat()[id_].size
            arreglo = self.verdicmat()[id_].reshape(1,size)
            return arreglo
        
    def arreglo(self, id_):
        catalogo = {}
        print('La información contenida en el archivo es la siguiente: ')
        for clave, info_ in self.verdicmat()[id_].items():
            for i in range(len(self.verdicmat()[id_])):
                print(f'''Posición {i}: El diccionario es "{clave}" y su Clave es:
                {info_}\n''')
                catalogo[i] = info_
        posicion = int(input('Eliga la posición del arreglo que desea usar: '))
        arreglo = catalogo[posicion]
        return arreglo
      
    def mostrarcolumnas(self, id_):
        listacolumnas = self.verdiccsv()[id_].columns
        for i in range(len(listacolumnas)):
            print(f'Las columnas del archivo son:  
                  {listacolumnas[i]}')
        return listacolumnas    
    def graficarcolumna(self, id_):
        tabla = self.verdiccsv()[id_]
        print('Esta es la visualización del archivo almacenado')
        while True:
            print(tabla)
            try:
                columna = input('Indique el nombre de la columna que posee datos númerico que desea graficar: ')
                print(f'''La tabla escogida es la siguiente: {tabla[columna]}''')
                break
            except KeyError:
                print('El nombre debe ser exactemente el mismo.')
        plt.scatter(tabla.index, tabla[columna])  # Utiliza los indices como valores para el eje x si tu DataFrame tiene un índice numérico
        plt.xlabel('Índice') 
        plt.ylabel('Valor de la columna')
        plt.title('Scatter de una columna')
        plt.grid(True)
        plt.show() 
    def crearcolumna(self, id_):
        while True:
            print(tabla)
            try:
                columna = input('Indique el nombre de la columna que posse datos númerico que desea graficar: ')
                print(f'''La tabla escogida es la siguiente: {tabla[columna]}''')
                break
            except KeyError:
                print('El nombre debe ser exactemente el mismo.')
        suma = self.__diccsv[id_]["Nueva Columna"] =  self.__diccsv[id_][c1, c2, c3, c4].sum(axis=1,skipna=True) 
        media = suma.mean()
        moda = 1
        desv = suma.std()
        return print(f'La nueva colmuna tiene una media, moda y desviación de {media}, {moda} y {desv} respectivamente.')


# Clase que se encarga de graficar todo arreglo. Como se exige una ubicación en particular de las gráficas
# se dispone de la figura de la siguiente manera: se crean 3 subplots que se ubicaran
class graficarmat:
    def __init__(self):
        self.__figura = plt.figure()
        self.__eje1 = self.__figura.add_subplot(2,3,3) #en la esquina superior derecha
        self.__eje2 = self.__figura.add_subplot(2,3,4) #en la esquina inferior izquierda
        self.__eje3 = self.__figura.add_subplot(2,3,5) #en la centro de la zona inferior

    def graf1(self, arreglo):
        print('\nGRÁFICA 1')
        shapev, shapeh = arreglo.shape
        print(f'Tiene disponible {shapev} canal(es) para graficar.')
        while True:
            canal1 = int(input('Seleccione el canal que desea graficar en la desviación estándar: '))
            if 0 < canal1 <= shapev:
                break
            else:
                print(f'Ingrese un valor entre 1 y {shapev}: ')
        x = np.random.randn(shapeh)
        leyenda = input('Ingrese leyenda: ')
        titulo = input('Ingrese título: ')
        nomx = input('Ingrese etiqueta del eje x: ')
        nomy = input('Ingrese etiqueta del eje y: ')
        self.__eje1.scatter(x, arreglo[canal1,:], label=leyenda)
        self.__eje1.set_title(titulo)
        self.__eje1.set_xlabel(nomx)
        self.__eje1.set_ylabel(nomy)
        self.__eje1.legend()   
    def graf2(self, arreglo):
        print('\nGRÁFICA 2')
        sum = np.sum(arreglo, axis=0)
        shapeh = arreglo.shape[1]
        while True:
            a = int(input(f'Ingrese un valor entre 1 y {shapeh} para el límite inferior del segmento que desea graficar: '))
            b = int(input(f'Ingrese un valor entre 1 y {shapeh} para el límite superior del segmento que desea graficar: '))
            if a < b and 0 < a <= shapeh and 0 < b <= shapeh:
                break
            else:
                print(f'Ingrese un valor entre 1 y {shapeh} para cada segmento. Recuerde que el primer número debe ser menor que el segundo')
        leyenda2 = input('Ingrese leyenda: ')
        titulo2 = input('Ingrese título: ')
        nomx2 = input('Ingrese etiqueta del eje x: ')
        nomy2 = input('Ingrese etiqueta del eje y: ')
        self.__eje2.plot(sum[a:b], color='red', label=leyenda2)
        self.__eje2.set_title(titulo2)
        self.__eje2.set_xlabel(nomx2)
        self.__eje2.set_ylabel(nomy2)
        self.__eje2.legend() 
    def graf3(self, arreglo):
        print('\nGRÁFICA 3')
        shapev, shapeh = arreglo.shape
        print(f'Tiene disponible {shapev} canal(es) para graficar.')
        while True:
            canal2 = int(input('Seleccione el canal que desea graficar con ruido: '))
            if 0 < canal2 <= shapev:
                break
            else:
                print(f'Ingrese un valor entre 1 y {shapev}')
        shape = arreglo.shape
        x2 = np.random.randn(shapeh)
        arreglo2 = arreglo+np.random.random(shape)
        leyenda3 = input('Ingrese leyenda: ')
        titulo3 = input('Ingrese título: ')
        nomx3 = input('Ingrese etiqueta del eje x: ')
        nomy3 = input('Ingrese etiqueta del eje y: ')
        self.__eje3.plot(x2, arreglo2[canal2,:], color='yellow', label=leyenda3)
        self.__eje3.set_title(titulo3)
        self.__eje3.set_xlabel(nomx3)
        self.__eje3.set_ylabel(nomy3)
        self.__eje3.legend()
    
#     # def nuevacolumna(self, c1, c2, c3, c4, id_):
#     #     suma = self.__diccsv[id_]["Nueva Columna"] =  self.__diccsv[id_][c1, c2, c3, c4].sum(axis=1,skipna=True) 
#     #     media = suma.mean()
#     #     moda = 1
#     #     desv = suma.std()
#     #     return print(f'La nueva colmuna tiene una media, moda y desviación de {media}, {moda} y {desv} respectivamente.')

def menu():
    obj = sistema()
    while True:
        op = int(input('''Seleccione una de las siguientes opciones:
                       
    1. Ingrese un archivo MAT
    2. Ingrese un archivo CSV
    3. Grafique una señal
    4. Mostrar información
    5. Salir
                       
    >> '''))
        if op == 1:
            id_ = int(input('Ingrese ID: '))
            if not obj.verificarexistecsv(id_):
                while True:
                    url = input('Ingrese URL del archivo: ')
                    try:
                        dic = sio.loadmat(url)
                        break
                    except FileNotFoundError:
                        print('Archivo no hallado')
                        continue
                obj.agregaramat(id_, dic)
            else:
                print('El ID ya se encuentra registrado')
        elif op == 2:
            id_ = int(input('Ingrese ID: '))
            if not obj.verificarexistemat(id_):
                while True:
                    url = input('Ingrese URL del archivo: ')
                    try:
                        tabla = pd.read_csv(url)
                        break
                    except FileNotFoundError:
                        print("Archivo no hallado")
                        continue
                obj.agregaracsv(id_, tabla)
            else:
                print('El ID ya se encuentra registrado')
        elif op == 3:
            figura = graficarmat()
            id_ = int(input('Ingrese ID a graficar: '))
            if obj.verificarexistemat(id_):
                arreglo = obj.arreglo(id_)
                figura.graf1(arreglo)
                figura.graf2(arreglo)
                figura.graf3(arreglo)
                plt.grid(True)
                plt.tight_layout() # Ajusta automáticamente los subplots para que no haya superposición
                plt.show() # Mostrar la figura
            else:
                print("El ID ingresado no se encuentra registrado")
        elif op == 4:
            id_ = int(input('Ingrese ID a graficar: '))
            print(obj.mostrarcolumnas(id_))
            obj.graficarcolumna(id_)
            


        elif op == 5:
            break
        else:
            print('Opción existente en el menú')

if __name__ == '__main__':
    menu()
