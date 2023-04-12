# Programa para calcular las pulsaciones por 10 segundos en ejercicio aerobico
edad = int(input("Ingrese su edad en años: "))
genero = int(input("Ingrese su género (1 para femenino y 2 para masculino): "))

if genero == 1:
    pulsaciones = (220 - edad) / 10
elif genero == 2:
    pulsaciones = (210 - edad) / 10
else:
    pulsaciones = 0
    print("Género ingresado no válido.")

if pulsaciones != 0:
    print("Número de pulsaciones por 10 segundos de ejercicio aeróbico:", pulsaciones)