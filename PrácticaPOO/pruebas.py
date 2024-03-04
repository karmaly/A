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
    

nm = int(input("numero"))
listanombre_med = []
lista_med = []
for i in range(0,nm):
    while True:
        nombre_med = input("Ingrese el nombre del medicamento: ")
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