def remove_duplicates(lista):
    result = []
    for item in lista:
        if item not in result:
            result.append(item)
    return result

# Prueba el programa con una lista con duplicados
numbers = [2, 3, 5, 2, 7, 3, 5]
print("Lista sin duplicados:", remove_duplicates(numbers))