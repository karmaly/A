from clase4G2_ import *

def main():
    mi_sistema = Sistema()

    while True:
        opcion = int(input("1. Nuevo paciente\n - 2. Numero de paciente\n - 3. Datos paciente\n - 4. Salir:  \n"))
        if opcion == 1:
            mi_sistema.ingresarPaciente()
        elif opcion == 2:
            print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()))
        elif opcion == 3:
            mi_sistema.verDatosPaciente()
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")
    
    
if __name__ == '__main__':
    main()

    