def invertir_cadena(cadena):
    cadena_invertida = ""
    for char in cadena:
        cadena_invertida = char + cadena_invertida
    return cadena_invertida
cadena_original = "1234abcd"
cadena_invertida = invertir_cadena(cadena_original)
print(cadena_invertida) # Imprime "dcba4321"