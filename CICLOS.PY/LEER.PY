total = 0

for i in range(10):
    num = int(input("Ingrese un número: "))
    total += num

average = total / 10

print("Suma de los números:", total)
print("Promedio de los números:", average)