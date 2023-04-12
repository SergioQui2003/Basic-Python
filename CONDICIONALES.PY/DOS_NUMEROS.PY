number1 = int(input("Introduce el primer número: "))
number2 = int(input("Introduce el segundo número: "))

if number1 > number2:
    print("El mayor número es", number1, "y el menor número es", number2)
elif number1 < number2:
    print("El mayor número es", number2, "y el menor número es", number1)
else:
    print("Los números son iguales.")