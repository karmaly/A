class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = int
#Getters class Medicamento
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
#Setters class Medicamento
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    def __init__(self):
        self.__nombre= " "
        self.__historia = int
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
#Getters class Mascota  
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
#Setters class Mascota
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
    
class sistemaV:
    def __init__(self):
        self.__lista_felinos = {}
        self.__lista_caninos = {}
#Getters class sistevaV
    def verDicFel(self):
        return self.__lista_felinos
    
    def verDicCan(self):
        return self.__lista_caninos
    
#Funciones class Sistema
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
        if self.verificarExiste(historia):
            if tipo == "Felino":
                return self.verDicFel(self)[historia].verFecha()
        else:
            return self.verDicCan()[historia].verFecha()

    def verMedicamento(self,historia,tipo):
        if self.verificarExiste(historia):
            if tipo == "Felino":
                return self.verDicFel()[historia].verLista_Medicamentos()
        else:
            return self.verDicCan()[historia].verLista_Medicamentos()
    
    def eliminarMascota(self,historia,tipo):
        if self.verificarExiste(historia):
            if tipo == "Felino":
                del self.verDicFel(self)[historia]
                return print(f"La mascota con {historia} fue eliminada")
        else:
            del self.verDicCan(self)[historia]
            return print(f"La mascota con {historia} fue eliminada")
    
    def verNumeroMascotas(self):
        return len(self.__lista_felinos) + len(self.__lista_caninos)

# Funcion para validar entero
def validarNumero(numero):
    try:
        a = int(numero)
        return True
    except ValueError:
        return False

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
            opc = validarNumero(menu)
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
            while True:
                tipov=input("Ingrese el tipo de mascota: 1. Felino o 2. Canino): ")
                t = validarNumero(tipov)
                if t:
                    if tipov == 1:
                        tipo = "Felino"
                        break
                    elif tipov == 2:
                        tipo ="Canino"
                        break
                    else:
                        print("Elija una de las dos opciones")
                else: 
                    print("Ingrese 1 o 2 como indican las opciones disponibles")
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                while True:
                    pesov=input("Ingrese el peso de la mascota: ")
                    p = validarNumero(pesov)
                    if p:
                        peso = int(pesov)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")   
                while True:
                    nmv=int(input("Ingrese cantidad de medicamentos: "))
                    nu = validarNumero(nmv)
                    if nu:
                        nm = int(nmv)
                        break
                    else:
                        print("Debe ser un dato numérico (sin puntos ni letras)")   
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

