total = 0
# escribo la formula para que me pueda dar el promedio de un número 
for i in range(5):
    numero = float(input("Registre un número: "))
    total += numero
# imprime el promedio de los 5 números dados 
promedio = total / 5
print("El promedio es:", promedio)