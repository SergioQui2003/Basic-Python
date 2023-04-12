def contar_letras(cadena):
    letras_mayusculas = 0
    letras_minusculas = 0

    for letra in cadena:
        if letra.isupper():
            letras_mayusculas += 1
        elif letra.islower():
            letras_minusculas += 1

    print("Número de letras mayúsculas: ", letras_mayusculas)
    print("Número de letras minúsculas: ", letras_minusculas)