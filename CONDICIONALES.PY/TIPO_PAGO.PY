print("Bienvenido al programa de selección de método de pago")
cuenta = float(input("Ingrese el monto de la cuenta: "))

if cuenta < 150000:
    print("El método de pago recomendado es en efectivo")
elif cuenta >= 150000 and cuenta < 300000:
    print("El método de pago recomendado es dinero electrónico")
elif cuenta >= 300000 and cuenta < 600000:
    print("El método de pago recomendado es tarjeta de débito")
else:
    print("El método de pago recomendado es tarjeta de crédito")