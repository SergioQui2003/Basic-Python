def elementos_unicos(lista):
    lista_unicos = []

    for elemento in lista:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)

    return lista_unicos
lista = [1, 2, 2, 3, 3, 3, 4, 5, 5]
lista_unicos = elementos_unicos(lista)
print(lista_unicos)