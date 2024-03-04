from datetime import datetime

# Función para validar entero
def validarNumero(numero):
    try:
        a = int(numero)
        return True
    except ValueError:
        return False
    
# Función para validar Fecha
def verificar_formato_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
        return True, fecha
    except ValueError:
        return False, None
    
# Función para validar tipo  

def tipe():
    while True:
        tipov = input("Ingrese el tipo de mascota (1. Felino o 2. Canino): ")
        if validarNumero(tipov):  # Verifica si la entrada es un número
            tipov = int(tipov)  # Convierte la entrada a entero
            if tipov == 1:
                tipo = "Felino"
                return tipo
            elif tipov == 2:
                tipo = "Canino"
                return tipo
            else:
                print("Elija una de las dos opciones")
        else: 
            print("Ingrese 1 o 2 como indican las opciones disponibles")
    
# Creación class Medicamento
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = int
# Getters class Medicamento
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
# Setters class Medicamento
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med

# Creacción class Mascota
class Mascota:
    def __init__(self):
        self.__nombre= " "
        self.__historia = int
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
# Getters class Mascota  
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
# Setters class Mascota
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos=n 
    
# Creación class sistemaV
class sistemaV:
    def __init__(self):
        self.__lista_felinos = {}
        self.__lista_caninos = {}

# Getters class sistemaV
    def verDicFel(self):
        return self.__lista_felinos
    
    def verDicCan(self):
        return self.__lista_caninos
    
# Funciones class sistemaV
    def verificarExiste(self, historia):
        if historia in self.__lista_felinos or self.__lista_caninos:
            return True
        else:
            return False
    def ingresarMascota(self,tipo,historia,mas):
        if tipo == "Felino":
            self.verDicFel()[historia] = mas
            return print("Mascota tipo felino ingresada")
        else:
            self.verDicCan()[historia] = mas
        return print("Mascota tipo canino ingresada")
    
    def verFechaIngreso(self,historia,tipo):
        if tipo == "Felino":
            return self.verDicFel(self)[historia].verFecha()
        else:
            return self.verDicCan()[historia].verFecha()


    def verMedicamento(self,historia,tipo):
        if tipo == "Felino":
            return self.verDicFel()[historia].verLista_Medicamentos()
        else:
            return self.verDicCan()[historia].verLista_Medicamentos()

    
    def eliminarMascota(self,historia,tipo):
        if tipo == "Felino":
            del self.verDicFel(self)[historia]
            return print(f"La mascota con {historia} fue eliminada")
        else:
            del self.verDicCan(self)[historia]
            return print(f"La mascota con {historia} fue eliminada")
    
    def verNumeroMascotas(self):
        return len(self.__lista_felinos) + len(self.__lista_caninos)
    
def main():
    servicio_hospitalario = sistemaV()
    while True:
        while True:
            menuv = (input('''\nIngrese una opción: 
                        \n1- Ingresar una mascota
                        \n2- Ver fecha de ingreso 
                        \n3- Ver número de mascotas en el servicio 
                        \n4- Ver medicamentos que se están administrando
                        \n5- Eliminar mascota 
                        \n6- Salir 
                        \nUsted ingresó la opción: ''' ))
            opc = validarNumero(menuv)
            if opc:
                menu = int(menuv)
                break
            else:
                print("Selecione una opción del menú")
                continue
        if menu == 1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            while True:
                historiav=input("Ingrese la historia clínica de la mascota: ")
                h = validarNumero(historiav)
                if h:
                    historia = int(historiav)
                    break
                else:
                   print("Debe ser un dato numérico (sin puntos ni letras)")
                   continue
            if servicio_hospitalario.verificarExiste(historia) == False:
                tipo = tipe()
                nombre=input("Ingrese el nombre de la mascota: ")
                while True:
                    pesov=input("Ingrese el peso de la mascota: ")
                    p = validarNumero(pesov)
                    if p:
                        peso = int(pesov)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")
                        continue
                while True: 
                    fecha_in = input("Por favor, ingresa la fecha en formato dd/mm/aaaa: ")
                    es_formato_valido, fecha = verificar_formato_fecha(fecha_in)
                    if es_formato_valido:
                        fecha = fecha_in
                        break
                    else:
                        print("La fecha ingresada no tiene el formato dd/mm/aaaa.")
                        continue
                while True:
                    nmv=input("Ingrese cantidad de medicamentos: ")
                    nu = validarNumero(nmv)
                    if nu:
                        nm = int(nmv)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")
                        continue
                listanombre_med = []
                lista_med = []
                for i in range(0,nm):
                    while True:
                        nombre_med = input("Ingrese el nombre del medicamento: ").upper()
                        if nombre_med in listanombre_med:
                            print("El medicamento ya se encuenta agregado")
                            continue
                        else:
                            listanombre_med.append(nombre_med)
                            dosis = int(input("Ingrese la dosis: "))
                            medic = Medicamento()
                            medic.asignarNombre(nombre_med)
                            medic.asignarDosis(dosis)
                            lista_med.append(medic)
                            break

                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(tipo,historia,mas)
            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            while True:
                    bushc = input("Ingrese la historia clínica de la mascota: ")
                    bus = validarNumero(bushc)
                    if bus:
                        busqhc = int(bushc)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")   
            if servicio_hospitalario.verificarExiste(busqhc):
                tipo = tipe()
                print(servicio_hospitalario.verFechaIngreso(busqhc,tipo))
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            while True:
                    bushc = input("Ingrese la historia clínica de la mascota: ")
                    bus = validarNumero(bushc)
                    if bus:
                        busqhc = int(bushc)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")   
            if servicio_hospitalario.verificarExiste(busqhc):
                tipo = tipe()
                print(f"Los medicamentos de la mascota con historia {busqhc} son:")
                for i in servicio_hospitalario.verMedicamento(busqhc,tipo):
                    print(i.verNombre())
                    print(i.verDosis())
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
        elif menu == 5: # Eliminar mascota
            while True:
                    bushc = input("Ingrese la historia clínica de la mascota: ")
                    bus = validarNumero(bushc)
                    if bus:
                        busqhc = int(bushc)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")   
            if servicio_hospitalario.verificarExiste(busqhc):
                tipo = tipe()
                print(servicio_hospitalario.eliminarMascota(busqhc,tipo))
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

