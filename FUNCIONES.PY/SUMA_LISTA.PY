def sumar_lista(numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma
numeros = (8, 2, 3, 0, 7)
suma_total = sumar_lista(numeros)
print(suma_total) # Imprime 20