print("Bienvenido al programa de compra de pizzas")
tamaño = int(input("Ingrese el tamaño de la pizza (1, 2 o 3): "))
ingredientes = int(input("Ingrese el número de ingredientes adicionales: "))

if tamaño == 1:
    precio = 15000
elif tamaño == 2:
    precio = 24000
elif tamaño == 3:
    precio = 36000
else:
    precio = 0
    print("Tamaño inválido, por favor ingrese un tamaño válido (1, 2 o 3)")

pago = precio + ingredientes * 4000
print("El valor total a pagar es: $" + str(pago))