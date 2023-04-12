def find_long_words(p, n):
    result = []
    for word in p:
        if len(word) > n:
            result.append(word)
    return result

# Prueba el programa con una lista de palabras y una longitud n
p = ['gato', 'ventana', 'defenderse', 'web']
n = 6
print("Palabras más largas que", n, ":", find_long_words(p, n))