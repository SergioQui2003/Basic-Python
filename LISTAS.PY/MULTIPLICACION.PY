def multiply_list(lista):
    result = 1
    for item in lista:
        result *= item
    return result

# Prueba el programa con una lista de números
numbers = [1, 2, 3, 4, 5]
print("El producto de los elementos de la lista es:", multiply_list(numbers))