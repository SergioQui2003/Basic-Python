def multiplicacion_de_3numeros (numero1, numero2, numero3):
    result = numero1 * numero2 * numero3
    return result

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

resultado = multiplicacion_de_3numeros(numero1, numero2, numero3)
print("El resultado es:", resultado)