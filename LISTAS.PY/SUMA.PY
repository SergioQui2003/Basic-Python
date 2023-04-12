def suma_lista(lista):
    result = 0
    for item in lista:
        result += item
    return result

# Prueba el programa con una lista de números
numbers = [1, 2, 3, 4, 5]
print("La suma de los elementos de la lista es:", suma_lista(numbers))