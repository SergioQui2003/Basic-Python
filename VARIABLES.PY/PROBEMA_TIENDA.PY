# espeficico cual es el problema que quiero realizar:Debe tener como entradas el valor unitario, la cantidad de productos comprados
# y al valor final se debe adicionar el 16% correspondiente al IVA.

valor_unitario = float(input("Ingrese el valor unitario: "))
cantidad = int(input("¿Cuantos productos ha comprado?: "))

#despues de recolectar la informacion hago la formula para que el valor me adicional con el IVA

subtotal = valor_unitario * cantidad
iva = 0.16 * subtotal
resultado = subtotal + iva

print("El valor final a pagar es:", resultado)