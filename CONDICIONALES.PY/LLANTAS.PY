print("Bienvenido al programa de compra de llantas")
cantidad = int(input("Ingrese la cantidad de llantas a comprar: "))

if cantidad < 6:
    precio = 240000
elif cantidad >= 6 and cantidad <= 7:
    precio = 221000
else:
    precio = 180000

pago = cantidad * precio
print("El valor total a pagar es: $" + str(pago))