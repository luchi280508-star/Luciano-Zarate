print("HORNO INDUSTRIAL")

while True:
    temperatura = input("Ingrese la temperatura del horno (en °C): ")
    if temperatura == "FIN":
        break 
    if temperatura == "" or temperatura == ".":
        print("Error: No se ingresó ninguna temperatura. Por favor, ingrese un valor válido.")
        continue
    if temperatura.count(".") > 1:
        print("Error: Se ingresó un valor no válido. Por favor, ingrese un número válido.")
        continue
    if not temperatura.replace(".", "").isdigit():
        print("Error: Se ingresó un valor no válido. Por favor, ingrese un número válido.")
        continue
    temperatura = float(temperatura)
    if temperatura < 100.0 or temperatura > 500.0:
        print("!Advertencia! temperatura fuera de rango")
