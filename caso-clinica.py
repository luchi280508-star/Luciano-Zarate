print("Bienvenido a la clínica")

especialidades = []
cupos = []


while True: 
    print("1. ingrese las especialidades:")
    print("2. ingrese los cupos:")
    print("3. mostrar agenda")
    print("4. consultar cupos disponibles")
    print("5. listar especialidades sin cupos")
    print("6. agregar especialidad y cupos nuevos")
    print("7. actualizar cupos (resrvar / cancelar)")
    print("8. salir")    

    opcion = input("Ingrese un numero del 1 al 8 para seleccionar una opción: ")
    while not opcion.isdigit():
        print("Por favor, ingrese un número válido.")
        opcion = input("Ingrese una opción del 1 al 8: ")
    match opcion:
        case "1": 
            especialidad = input("Ingrese la especialidad: ")
            especialidades.append(especialidad)
            print(especialidades) 
        case "2":
            cupos_cantidad = input("Ingrese la cantidad de cupos para la especialidad: ")
            while not cupos_cantidad.isdigit() or int(cupos_cantidad) < 0:
                print("Por favor, ingrese un número válido de cupos (mayor o igual a 0).")
                cupos_cantidad = input("Ingrese la cantidad de cupos para la especialidad: ")
            cupos.append(cupos_cantidad)
            print(cupos)
        case "3":
            print("Agenda:")
            print("especialidades:", especialidades)
            print("cupos:", cupos)
        case "4":
            print("ingrese la especialidad que desee consultar cupos disponibles:")
            especialidad_consulta = input("Ingrese la especialidad: ")
            if especialidad_consulta in especialidades:
                for i in range(len(especialidades)):
                    if especialidades[i] == especialidad_consulta:
                        print(f"Cupos disponibles para {especialidad_consulta}: {cupos[i]}")
                        break
        case "5":
            print("Especialidades sin cupos:")
            for i in range(len(cupos)):
                if cupos[i] == "0":
                    print(f"{especialidades[i]}")
                    print(f"no hay mas especialidades sin cupos disponibles")
        case "6":
            nueva_especialidad = input("Ingrese la nueva especialidad: ")
            while nueva_especialidad in especialidades:
                print("La especialidad ya existe. Por favor, ingrese una especialidad diferente.")
                nueva_especialidad = input("Ingrese la nueva especialidad: ")
            nuevo_cupo = input("Ingrese la cantidad de cupos para la nueva especialidad:")
            while not nuevo_cupo.isdigit() or int(nuevo_cupo) < 0:
                print("Por favor, ingrese un número válido de cupos (mayor o igual a 0).")
                nuevo_cupo = input("Ingrese la cantidad de cupos para la nueva especialidad:")
            especialidades += (nueva_especialidad,)
            cupos += (nuevo_cupo,)
            print(f"Se ha agregado la especialidad {nueva_especialidad} con {nuevo_cupo} cupos.")
        case "7":
            print("turnos (reservar / cancelar):")
            turno = input("Ingrese la especialidad para reservar o cancelar un turno: ")
            if turno in especialidades:
                for i in range(len(especialidades)):
                    if especialidades[i] == turno:
                        accion = input("Ingrese 'reservar' para reservar un turno o 'cancelar' para cancelar un turno: ")
                        if accion == "reservar":
                            if int(cupos[i]) > 0:
                                cupos[i] = str(int(cupos[i]) - 1)
                                print(f"Se ha reservado un turno para {turno}. Cupos restantes: {cupos[i]}")
                            else:
                                print(f"No hay cupos disponibles para {turno}.")
                        elif accion == "cancelar":
                            cupos[i] = str(int(cupos[i]) + 1)
                            print(f"Se ha cancelado un turno para {turno}. Cupos disponibles: {cupos[i]}")
                        else:
                            print("Acción no válida. Por favor, ingrese 'reservar' o 'cancelar'.")
                        break
        case "8":
            print("salir")    