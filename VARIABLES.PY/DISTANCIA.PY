# Solicitar al usuario una distancia en metros y transformar a km., cm. o mm

def conversion_distancia(distancia, unidad):
    if unidad == "km":
        return distancia / 1000
    elif unidad == "cm":
        return distancia * 100
    elif unidad == "mm":
        return distancia * 1000
    else:
        return "Unidad no válida. Por favor, especifique km, cm o mm."

distancia = float(input("Introduce una distancia en metros: "))
unit = input("Introduce la unidad de conversión (km, cm o mm): ")
print(conversion_distancia(distancia, unit))