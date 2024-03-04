print("Ingrese para:\n0. Para volver al menu \n1. Ingresar nuevo paciente \n2. Ver paciente \n3. Ver cantidad de pacientes \n>> ")
def tipo():
    while True:
        tipov = input("Ingrese el tipo de mascota: 1. Felino o 2. Canino): ")
        t = validarNumero(tipov)
        if t:
            if tipov == 1:
                tipo = "Felino"
                return tipo
            elif tipov == 2:
                tipo = "Canino"
                return tipo
            else:
                print("Elija una de las dos opciones")
                continue
        else: 
            print("Ingrese 1 o 2 como indican las opciones disponibles")
            continue

a = tipo()
