cantidad = int(input("Ingrese la cantidad de productos a comprar: "))
precio_unitario = int(input("Ingrese el precio unitario del producto: "))

if cantidad <= 5:
    total = cantidad * precio_unitario
elif cantidad > 5 and cantidad < 10:
    total = cantidad * precio_unitario * 0.95
else:
    total = cantidad * precio_unitario * 0.92

print("El total a pagar es: $" + str(total))