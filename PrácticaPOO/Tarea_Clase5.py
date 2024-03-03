#Creación de objeto Paciente
class Paciente:
    def __init__(self):
        #Atributos
        self.__nombre = ""
        self.__cedula = int
        self.__genero = ""
        self.__servicio = ""

#Getters del objeto Paciente
    def verNombre(self):
        return self.__nombre  
    def verServicio(self):
        return self.__servicio 
    def verGenero(self):
        return self.__genero   
    def verCedula(self):
        return self.__cedula
    
#Setters del objeto Paciente
    def asignarNombre(self,n):
        self.__nombre = n   
    def asignarServicio(self,s):
        self.__servicio = s  
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

#Creación de objeto Sistema
class Sistema:
    def __init__(self):
        #Atributos
        self.__lista_pacientes = []

#Funciones del objeto paciente 
    def validarNumero(self, numero):
        try:
            a = int(numero)
            return True
        except ValueError:
            return False
    
    def verificarPac(self,cedula):
        encontrado = False
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                encontrado = True
                break
        return encontrado
 
    def verDatosPaciente(self,cedula):
        if self.verificarPac(cedula) == False:
            return None
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return p
                       
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

#Creación de función main para iniciar el código:    
def main():
    sis = Sistema()
    while True:
        opcionv = input("Ingrese para:\n0. Para volver al menu \n1. Ingresar nuevo paciente \n2. Ver paciente \n3. Ver cantidad de pacientes \n>> ")
        a = validarNumero(opcionv)
        if a:
            opcion = int(opcionv)
            if opcion == 1:
                print("A continuacion se solicitaran los seguientes datos:\n")
                # 1 Se solicitaran los datos
                nombre = input("Ingrese el nombre: ")
                while True:
                    cedulav = input("Ingrese la cedula: ")
                    c = validarNumero(cedula)
                    if c:
                        cedula = int(cedulav)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")
                        continue
                genero = input("Ingrese el genero: ")
                servicio = input("Ingrese el servicio: ")
                # 2 se crea un objeto Paciente
                pac = Paciente()
                # como es paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(nombre)
                pac.asignarCedula(cedula)
                pac.asignarGenero(genero)
                pac.asignarServicio(servicio)
                r = sis.ingresarPaciente(pac)
                # 3 se almacena en la lista que esta dentro de la clase sistema
                if r == True:
                    print("paciente ingresado")
                else:
                    print("paciente ya existe en el sistema")

            elif opcion == 2:
                # 1 solicito la cedula que quiero buscar
                while True:
                    cedulav = input("Ingrese la cedula a buscar: ")
                    c = validarNumero(cedula)
                    if c:
                        cedula = int(cedulav)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")
                        continue
                # le pido al sistema que me devuelva en la variable p al paciente que tenga
                #  la cedula c en la lista
                p = sis.verDatosPaciente(cedula)
                # si encunetro el paciente imprimo los datos
                if p == None:
                    print("El paciente no se encotró")
                else:
                    print("Nombre: " + p.verNombre())
                    print("Cedula: " + str(p.verCedula()))
                    print("Genero: " + p.verGenero())
                    print("Servicio: " + p.verServicio())
            
            elif opcion == 3:
                print(f"la cantidad de pacientes en el sistema es: {sis.verNumeroPacientes()}")
                        
            elif opcion != 0:
                continue
        else:
            break

if __name__ == '__main__':
    main()