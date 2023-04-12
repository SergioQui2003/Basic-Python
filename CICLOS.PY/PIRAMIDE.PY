rows = int(input("Ingrese el número de filas: "))

for i in range(1, rows+1):
    for j in range(rows-i):
        print(end=" ")
    for k in range(1, i+1):
        print(k, end=" ")
    print()