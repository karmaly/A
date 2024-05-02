# Importo Clases con todas sus funciones
from Clases import *

def menu():
    obj = sistema()
    while True:
        op = int(input('''\nSeleccione una de las siguientes opciones: \n\n1. Ingrese un archivo MAT \n2. Ingrese un archivo CSV \n3. Grafique una señal \n4. Mostrar información \n5. Salir \n\n>> '''))
        if op == 1:
            id_ = int(input('Ingrese ID: '))
            if not obj.verificarexistemat(id_):
                while True:
                    url = input('Ingrese URL del archivo: ')
                    try:
                        dic = sio.loadmat(url)
                        break
                    except FileNotFoundError:
                        print('Archivo no hallado')
                    except ValueError:
                        print('Tipo de archivo incorrecto')
                obj.agregaramat(id_, dic)
            else:
                print('El ID ya se encuentra registrado')
        elif op == 2:
            id_ = int(input('Ingrese ID: '))
            if not obj.verificarexistecsv(id_):
                while True:
                    url = input('Ingrese URL del archivo: ')
                    try:
                        tabla = pd.read_csv(url)
                        break
                    except FileNotFoundError:
                        print('Archivo no hallado')
                    except ValueError:
                        print('Tipo de archivo incorrecto')
                obj.agregaracsv(id_, tabla)
            else:
                print('El ID ya se encuentra registrado')
        elif op == 3:
            figura = graficarmat()
            id_ = int(input('Ingrese ID a graficar: '))
            if obj.verificarexistemat(id_):
                arreglo = obj.dimensionado(id_)
                figura.graf1(arreglo)
                figura.graf2(arreglo)
                figura.graf3(arreglo)
                plt.tight_layout() # Ajusta automáticamente los subplots para que no haya superposición
                plt.show() # Mostrar la figura
            else:
                print("El ID ingresado no se encuentra registrado")
        elif op == 4:
            id_ = int(input('Ingrese ID a graficar: '))
            if obj.verificarexistecsv(id_):
                obj.mostrarcolumnas(id_)
                obj.graficarcolumna(id_)
                obj.crearcolumna(id_)
            else:
                print('El ID no se encuentra en la base de datos.')
        elif op == 5:
            break
        else:
            print('Opción existente en el menú')

if __name__ == '__main__':
    menu()
