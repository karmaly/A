import re
# Creación de objeto Paciente
class Paciente:
    def __init__(self):
        # Atributos
        self.__nombre = ""
        self.__cedula = int
        self.__genero = ""
        self.__servicio = ""

# Getters del objeto Paciente
    def verNombre(self):
        return self.__nombre  
    def verServicio(self):
        return self.__servicio 
    def verGenero(self):
        return self.__genero   
    def verCedula(self):
        return self.__cedula
    
# Setters del objeto Paciente
    def asignarNombre(self,n):
        self.__nombre = n   
    def asignarServicio(self,s):
        self.__servicio = s  
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

# Creación de objeto Sistema
class Sistema:
    def __init__(self):
        # Atributos
        self.__lista_pacientes = []

# Funciones del objeto paciente 
    def verificarPac(self,cedula):
        encontrado = False
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                encontrado = True
                break
        return encontrado
 
    #def verDatosPaciente(self,cedula):
    #    if self.verificarPac(cedula) == False:
    #        return None
    #    for p in self.__lista_pacientes:
    #        if cedula == p.verCedula():
    #            return p
                       
    def ingresarPaciente(self,pac):
        if self.verificarPac(pac.verCedula()):
            return False
        self.__lista_pacientes.append(pac)
        return True

    def eliminarPaciente(self,cedula):
        if self.verificarPac(cedula) == False:
            return None
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                del self.__lista_pacientes[cedula]
                break
            return True
        
    def verNumeroPacientes(self):
        return len(self.__lista_pacientes)
    
def validarNumero(numero):
    try:
        a = int(numero)
        return True
    except ValueError:
        return False
    
# Creación de función main para iniciar el código:    
def main():
    sis = Sistema()
    while True:
        opcionv = input("\nIngrese para:\n0. Volver al menu \n1. Ingresar nuevo paciente \n2. Ver paciente \n3. Ver cantidad de pacientes \n>> ")
        a = validarNumero(opcionv)
        if a:
            opcion = int(opcionv)
            if opcion == 1:
                print("\nA continuacion se solicitaran los seguientes datos:\n")
                # 1. Se solicitaran los datos
                nombre = input("Ingrese el nombre: ")
                while True:
                    cedulav = input("Ingrese la cedula: ")
                    c = validarNumero(cedulav)
                    if c:
                        cedula = int(cedulav)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")
                        continue
                genero = input("Ingrese el genero: ")
                servicio = input("Ingrese el servicio: ")
                # 2. Se crea un objeto Paciente
                pac = Paciente()
                # Como es paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(nombre)
                pac.asignarCedula(cedula)
                pac.asignarGenero(genero)
                pac.asignarServicio(servicio)
                r = sis.ingresarPaciente(pac)
                # 3 Se almacena en la lista que esta dentro de la clase sistema
                if r == True:
                    print("Paciente ingresado")
                else:
                    print("Paciente ya existe en el sistema")

            elif opcion == 2:
                # 1. Solicito el nombre o cedula que quiero buscar
                while True:
                    busquedav: input("\nIngrese para:\n0. Busqueda por cédula o parte de ella \n1. Nombre o parte de él\n>> ")
                    a = validarNumero(busquedav)
                    if a:
                        busqueda = int(busquedav)
                        if busqueda == 0:
                            while True:
                                cedulav = input("Ingrese la cedula o parte de ella: ")
                                c = validarNumero(cedula)
                                if c:
                                    cedula = int(cedulav)
                                    break
                                else:
                                    print("Debe ser un dato numérico (sin puntos ni letras)")
                                    continue
                        # Le pido al sistema que me devuelva en la variable p al paciente que tenga
                        # la cedula en la lista
                            patron = re.complie(f".*{cedula}.*")
                            c = 0
                            for cedula in sis:
                                if patron.match(cedula.verCedula()):
                                    # Si encunetro el paciente imprimo los datos
                                    c += 1
                                    print("Nombre: " + p.verNombre())
                                    print("Cedula: " + str(p.verCedula()))
                                    print("Genero: " + p.verGenero())
                                    print("Servicio: " + p.verServicio())
                                else: 
                                    print("No se tiene coincidencias.")
                        if busqueda == 1:
                            nombre = input("Ingrese el nombre o parte de él: ")
                        # Le pido al sistema que me devuelva en la variable p al paciente que tenga
                        # la cedula en la lista
                        patron = re.complie(f".*{cedula}.*")
                        for cedula in sis:
                            if patron.match(cedula.verCedula()):
                                # Si encunetro el paciente imprimo los datos
                                print("Los pacientes que tienen valores similares a la cédula buscada son:")
                                print("Nombre: " + p.verNombre())
                                print("Cedula: " + str(p.verCedula()))
                                print("Genero: " + p.verGenero())
                                print("Servicio: " + p.verServicio())
                            else: 
                                print("No se tiene coincidencias.")
                    else: 
                        print("Ingrese una opción válida")
            elif opcion == 3:
                print(f"La cantidad de pacientes en el sistema es: {sis.verNumeroPacientes()}")
                        
            elif opcion != 0:
                continue
        else:
            print("Seleccione una opción valida")
            continue

if __name__ == '__main__':
    main()