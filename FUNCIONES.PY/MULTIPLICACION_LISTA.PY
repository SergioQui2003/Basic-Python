def multiplicar_lista(numeros):
    producto = 1
    for num in numeros:
        producto *= num
    return producto
numeros = (8, 2, 3, -1, 7)
producto_total = multiplicar_lista(numeros)
print(producto_total) # Imprime -336