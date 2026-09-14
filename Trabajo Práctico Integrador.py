#actividad 1

while True:
    nombre = input("ingrese su nombre: ")
    if nombre.isalpha():
        break
    print("Error: El nombre debe contener solo letras. Intente nuevamente.")
while True:
    productos = input("ingrese la cantidad de productos q desee comprar: ")
    if productos.isdigit():
        productos = int(productos)
        if productos > 0:
           break
    print("Error: La cantidad de productos debe ser un número entero. Intente nuevamente.")
total_sin_descuento = 0
total_con_descuento = 0.0
for i in range(productos):
    while True:
        precio = input(f"ingrese el precio del producto {i + 1}: ")
        if precio.isdigit():
            precio = int(precio)
            break
        print("Error: El precio debe ser un número positivo. Intente nuevamente.")
    while True:
        descuento = input("tiene descuento? (s/n): ").lower()
        if descuento == "s" or descuento == "n":
            break
        print("Error: Debe ingresar 's' para sí o 'n' para no. Intente nuevamente.")
    total_sin_descuento += precio
    if descuento == "s":
        precio_final = precio * 0.9
    else:
        precio_final = float(precio)
    total_con_descuento += precio_final
    ahorro = total_sin_descuento - total_con_descuento
    promedio = total_con_descuento / productos

    print(f"\ncliente: {nombre}")
    print(f"cantidad de productos: {productos}")
    print(f"total sin descuento: ${total_sin_descuento}")
    print(f"total con descuento: ${total_con_descuento:.2f}")
    print(f"ahorro: ${ahorro:.2f}")
    print(f"promedio por producto: ${promedio:.2f}")

#atividad 2    
usuario_correcto = "alumno"
clave_correcta = "python123"
acceso = False

for intento in range(1, 4):
    usuario = input(f"intento {intento}/3 - usuario: ")
    clave = input("Ingrese su clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        break
    else:
        print(f"Usuario o clave incorrectos. Intento {intento} de 3.")
if not acceso:
        print("Cuenta bloqueada.")
else: 
    opcion = ""
    while True: 
        print("1. estado de cuenta: " )
        print("2. cambiar clave: ")
        print("3. mensajes: ")
        print("4. salir: ")
        opcion = input("Seleccione una opción: ")
        if not opcion.isdigit():
           print("Error: Debe ingresar un número. Intente nuevamente.")
        elif int(opcion) < 1 or int(opcion) > 4:
           print("Error: Opción inválida. Intente nuevamente.")    
        else:
            opcion = int(opcion)
            if opcion == 1:
                    print("inscripto")
            elif opcion == 2:
                    nueva_clave = input("Ingrese su nueva clave: ")
                    if len(nueva_clave) < 6:
                       print("Error: La clave debe tener al menos 6 caracteres. Intente nuevamente.")
                    else: 
                       confirmacion = input("Confirme su nueva clave: ")
                    if  confirmacion != nueva_clave:
                         print("Error: Las claves no coinciden. Intente nuevamente.")
                    else:
                        clave_correcta = nueva_clave
                        print("Clave cambiada exitosamente.")
            elif opcion == 3:
                  print("segui esforzandote, vas por buen camino.")
            elif opcion == 4:
                     print("Saliendo del sistema...")
                     break
#actividad 3
while True:
    operador = input("Nombre del operador: ")

    if operador.isalpha():
        break

    print("Error: ingresá solo letras.")


lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

print(f"Bienvenido/a, {operador}")

while True:
    print("\n1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingresá un número.")
       

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: elegí una opción entre 1 y 5.")
        

    if opcion == 5:
        print("Sistema cerrado.")
        break

    if opcion == 1 or opcion == 2 or opcion == 3:
        while True:
            dia = input("Día (1=Lunes, 2=Martes): ")

            if dia.isdigit():
                dia = int(dia)

                if dia == 1 or dia == 2:
                    break

            print("Error: elegí 1 o 2.")

   
    if opcion == 1:
        while True:
            nombre = input("Nombre del paciente: ")

            if nombre.isalpha():
                nombre = nombre.lower()
                break

            print("Error: ingresá solo letras.")

        if dia == 1:
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("El paciente ya tiene un turno el lunes.")
            elif lunes1 == "":
                lunes1 = nombre
                print("Reservado: lunes, turno 1.")
            elif lunes2 == "":
                lunes2 = nombre
                print("Reservado: lunes, turno 2.")
            elif lunes3 == "":
                lunes3 = nombre
                print("Reservado: lunes, turno 3.")
            elif lunes4 == "":
                lunes4 = nombre
                print("Reservado: lunes, turno 4.")
            else:
                print("No hay turnos disponibles el lunes.")

        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("El paciente ya tiene un turno el martes.")
            elif martes1 == "":
                martes1 = nombre
                print("Reservado: martes, turno 1.")
            elif martes2 == "":
                martes2 = nombre
                print("Reservado: martes, turno 2.")
            elif martes3 == "":
                martes3 = nombre
                print("Reservado: martes, turno 3.")
            else:
                print("No hay turnos disponibles el martes.")

   
    elif opcion == 2:
        while True:
            nombre = input("Nombre del paciente a cancelar: ")

            if nombre.isalpha():
                nombre = nombre.lower()
                break

            print("Error: ingresá solo letras.")

        if dia == 1:
            if nombre == lunes1:
                lunes1 = ""
                print("Turno cancelado.")
            elif nombre == lunes2:
                lunes2 = ""
                print("Turno cancelado.")
            elif nombre == lunes3:
                lunes3 = ""
                print("Turno cancelado.")
            elif nombre == lunes4:
                lunes4 = ""
                print("Turno cancelado.")
            else:
                print("El paciente no tiene turno el lunes.")

        else:
            if nombre == martes1:
                martes1 = ""
                print("Turno cancelado.")
            elif nombre == martes2:
                martes2 = ""
                print("Turno cancelado.")
            elif nombre == martes3:
                martes3 = ""
                print("Turno cancelado.")
            else:
                print("El paciente no tiene turno el martes.")


    elif opcion == 3:
        if dia == 1:
            print("\nAgenda del lunes")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")

        else:
            print("\nAgenda del martes")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")

    
    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print(f"\nLunes: {ocupados_lunes} ocupados, {disponibles_lunes} disponibles.")
        print(f"Martes: {ocupados_martes} ocupados, {disponibles_martes} disponibles.")

        if ocupados_lunes > ocupados_martes:
            print("Lunes tiene más turnos ocupados.")
        elif ocupados_martes > ocupados_lunes:
            print("Martes tiene más turnos ocupados.")
        else:
            print("Empate: ambos días tienen la misma cantidad de turnos ocupados.")

#actividad 4 
while True:
    nombre = input("Nombre del agente: ")

    if nombre.isalpha():
        nombre = nombre.capitalize()
        break

    print("Error: ingresá solo letras.")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0
bloqueado = False

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print(f"\nAgente: {nombre}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Código parcial: {codigo_parcial}")

    if alarma:
        print("Alarma: ON")
    else:
        print("Alarma: OFF")

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    while True:
        opcion = input("Elegí una opción: ")

        if opcion.isdigit():
            opcion = int(opcion)

            if opcion >= 1 and opcion <= 3:
                break

        print("Error: ingresá un número entre 1 y 3.")

    if opcion == 1:
        forzar_seguidas += 1
        riesgo = energia < 40

        energia -= 20
        tiempo -= 2

        if forzar_seguidas >= 3:
            alarma = True
            print("La cerradura se trabó. Se activó la alarma.")

        else:
            if riesgo:
                while True:
                    numero = input("Riesgo de alarma. Elegí un número del 1 al 3: ")

                    if numero.isdigit():
                        numero = int(numero)

                        if numero >= 1 and numero <= 3:
                            break

                    print("Error: ingresá un número entre 1 y 3.")

                if numero == 3:
                    alarma = True
                    print("Se activó la alarma.")

            if not alarma:
                cerraduras_abiertas += 1
                print("Abriste una cerradura.")
            else:
                print("No se abrió la cerradura.")

    elif opcion == 2:
        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - Código: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("El hackeo abrió una cerradura.")
        else:
            print("Código incompleto. Necesitás seguir hackeando.")

    elif opcion == 3:
        forzar_seguidas = 0

        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10
            print("La alarma te hizo perder 10 de energía extra.")

        print("Descansaste.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

print("\nFin del juego")
print(f"Energía final: {energia}")
print(f"Tiempo final: {tiempo}")
print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")

if bloqueado:
    print("DERROTA: el sistema se bloqueó por la alarma.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: te quedaste sin energía o sin tiempo.")
else:
    print(f"VICTORIA: {nombre}, abriste la bóveda.")

#actividad 5
print("--- BIENVENIDO A LA ARENA ---")

while True:
    nombre = input("Nombre del Gladiador: ")

    if nombre.isalpha():
        nombre = nombre.capitalize()
        break

    print("Error: Solo se permiten letras.")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo})")
        print(f"Pociones: {pociones}")

        print("\n1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        while True:
            opcion = input("Opción: ")

            if opcion.isdigit():
                opcion = int(opcion)

                if opcion >= 1 and opcion <= 3:
                    break
                else:
                    print("Error: elegí una opción entre 1 y 3.")
            else:
                print("Error: Ingrese un número válido.")

        if opcion == 1:
            dano = float(ataque_pesado)

            if vida_enemigo < 20:
                dano = ataque_pesado * 1.5
                print("¡Golpe crítico!")

            dano_aplicado = int(dano)
            vida_enemigo -= dano_aplicado

            print(f"¡Atacaste al enemigo por {dano_aplicado} puntos de daño!")

        elif opcion == 2:
            print("¡Inicias una ráfaga de golpes!")

            for golpe in range(3):
                vida_enemigo -= 5
                print(" > Golpe conectado por 5 de daño")

        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Recuperaste 30 puntos de vida!")
            else:
                print("¡No quedan pociones!")

        turno_gladiador = False

    else:
        vida_jugador -= ataque_enemigo
        print(f"¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")

        turno_gladiador = True

if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")