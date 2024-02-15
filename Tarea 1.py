
class Patient:
    def __init__(self, name, id_, gen, service):
        self.__nombre = name
        self.__identi = id_
        self.__genero = gen
        self.__servicio = service
    
class Nurse(Patient):
    def __init__(self,turno):
        Patient.__init__(self)
        self.turno = turno
class Physian(Patient):
    def __init__(self, especiality):
        Patient.__init__(self)
        self.especialidad = especiality

i = []

while True:
    