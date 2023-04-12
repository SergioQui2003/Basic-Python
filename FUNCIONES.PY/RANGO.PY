def en_rango(numero, rango_minimo, rango_maximo):
    if numero >= rango_minimo and numero <= rango_maximo:
        return True
    else:
        return False
numero = 5
rango_minimo = 1
rango_maximo = 10
esta_en_rango = en_rango(numero, rango_minimo, rango_maximo)
print(esta_en_rango) # Imprime True