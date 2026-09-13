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
