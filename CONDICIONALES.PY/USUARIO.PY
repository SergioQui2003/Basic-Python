name = input("Introduce tu nombre: ")
age = int(input("Introduce tu edad: "))

if age < 0 or age > 100:
    print("Por favor ingresa una edad válida.")
elif age >= 18:
    print("Usted es mayor de edad, " + name + ".")
else:
    print("Usted es menor de edad, " + name + ".")