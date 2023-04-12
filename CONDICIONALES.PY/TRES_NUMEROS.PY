print("Bienvenido al programa para ordenar tres números")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

numbers = [num1, num2, num3]
numbers.sort()

print("Orden Ascendente: ", numbers)
print("Orden Descendente: ", numbers[::-1])