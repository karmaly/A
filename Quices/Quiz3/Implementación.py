from Clases import *

lista_pac = {}
lista_archivos = {}
a = lista_pac
b = lista_archivos

while True:
    menu = ValNumInt(input('''
                    MENÚ PRINCIPAL
                    1. Ingresar Paciente
                    2. Ingresar Imagen (JPG o NPG)
                    3. Rotar imagen 
                    4. Binarizar y transformar imagen
                    5. Salir
                    -> '''))
    if menu == 1:
        menu_1(a, b)
    elif menu ==2:
        menu_2(b)
    elif menu ==3:
        menu_3(a, b)
    elif menu == 4:
        clave = input('\nIngrese el ID del paciente: ')
        if clave in lista_pac:
            pac = lista_pac[clave]
            lista_arreglos = pac.arreglos()
            num_ima = len(lista_arreglos)
            while True:
                imagen = ValNumInt(input(f'\nEl ID escogido tiene {num_ima} imágenes. Escoga una de ellas para transformarla: '))
                if 1 <= imagen <= num_ima:
                    original = lista_arreglos[imagen-1]
                    grafica = Graficar_Guardar()
                    kernel = ValNumInt(input('Ingrese el tamaño del kernel: '))
                    nombrenuevo = (input(f'\nNombre del nuevo archivo: '))+'.png'
                    grafica.transmorfo(original, kernel, nombrenuevo)
                    break
                else: 
                    print(f'Debe escoger un valor entre 1 y {num_ima}')
        else:
            print('La ID no se halla en la base de datos')
    elif menu ==5:
        print('Gracias por usar nuestro sistema')
        print('=)')
        break
    else:
        print('\nPor favor seleccione una opción válida del menú')


