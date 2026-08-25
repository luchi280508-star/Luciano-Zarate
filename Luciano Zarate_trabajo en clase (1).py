saldo = 50000

print("1_consultar saldo")
print("2_ingresar dinero")
print("3_retirar dinero")
print("4_salir")

while True:
    opcion = input("Ingrese una opción del 1/4: ")
    while not opcion.isdigit():
        print("Por favor, ingrese un número válido.")
        opcion = input("Ingrese una opción del 1/4: ")
    match opcion: 
        case "1": 
            print("consultar saldo")
            print(f"Su saldo es: {saldo}")
        case "2": 
            print("Ingrese el monto a depositar: ")
            while not (monto := input()).isdigit():
                print("Por favor, ingrese un monto válido.")
                print("Ingrese el monto a depositar: ")
            monto = int(monto)
            saldo += monto
            print(f"Su nuevo saldo es: {saldo}")
        case "3":
            print("Ingrese el monto a retirar: ")
            while not (monto := input()).isdigit():
                print("Por favor, ingrese un monto válido.")
                print("Ingrese el monto a retirar: ")
            monto = int(monto)
            saldo -= monto
            print(f"Su nuevo saldo es: {saldo}")
        case _:
            print("salir")
            break



