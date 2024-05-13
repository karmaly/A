from Clases import *

dict_pac = {}
dict_archivos = {
    'dict_dicom' : {},
    'dict_imagenes' : {}
}

a = dict_pac
b = dict_archivos
c = dict_archivos['dict_imagenes']
d = dict_archivos['dict_dicom']

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
        menu_1(a, d)
    elif menu ==2:
        menu_2(c)
    elif menu ==3:
        menu_3(a)
    elif menu == 4:
        menu_4(c)
    elif menu ==5:
        print('Gracias por usar nuestro sistema')
        print('=)')
        break
    else:
        print('\nPor favor seleccione una opción válida del menú')
