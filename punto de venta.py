"Sistema de punto de venta para un local de comida rapida."


def pedir_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("El valor no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("Entrada invalida. Ingrese un numero entero.")


total = 0

while True:
    print("\n- PUNTO DE VENTA -")
    print("1. Agregar Hamburguesa ($4500)")
    print("2. Agregar Papas Fritas ($2000)")
    print("3. Agregar Bebida ($1500)")
    print("4. Pagar el pedido")
    print("5. Cancelar pedido y salir")

    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "1":
        total += 4500
        print(f"Hamburguesa agregada. Total actual: ${total}")

    elif opcion == "2":
        total += 2000
        print(f"Papas fritas agregadas. Total actual: ${total}")

    elif opcion == "3":
        total += 1500
        print(f"Bebida agregada. Total actual: ${total}")

    elif opcion == "4":
        if total == 0:
            print("El pedido esta vacio. Agregue un producto antes de pagar.")
            continue

        print(f"Total a pagar: ${total}")
        efectivo = 0

        while efectivo < total:
            entrega = pedir_numero("Ingrese el efectivo entregado: $")
            efectivo += entrega

            if efectivo < total:
                faltante = total - efectivo
                print(f"Efectivo insuficiente. Faltan ${faltante}.")

        vuelto = efectivo - total
        print(f"Pago realizado. Vuelto: ${vuelto}")
        print("Ticket cerrado. Listo para el siguiente cliente.")
        total = 0

    elif opcion == "5":
        total = 0
        print("Pedido cancelado. Programa finalizado.")
        break

    else:
        print("Opcion invalida. Ingrese un numero del 1 al 5.")