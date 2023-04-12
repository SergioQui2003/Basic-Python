print("Bienvenido al conversor de temperaturas")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("%.2f grados Celsius son %.2f grados Fahrenheit" % (celsius, fahrenheit))
elif opcion == 2:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("%.2f grados Fahrenheit son %.2f grados Celsius" % (fahrenheit, celsius))
else:
    print("Opción inválida")