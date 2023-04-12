def find_min(lista):
    min = lista[0]
    for item in lista:
        if item < min:
            min = item
    return min

# Prueba el programa con una lista de números
numbers = [6, 4, 2, 8, 5]
print("El número más pequeño de la lista es:", find_min(numbers))