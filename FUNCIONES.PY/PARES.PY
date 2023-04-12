def numeros_pares(lista):
    numeros_pares = []
    for numero in lista:
        if numero % 2 == 0:
            numeros_pares.append(numero)

    return numeros_pares
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = numeros_pares(lista)
print(pares)