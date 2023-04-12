def main():
    print("Cálculo de áreas de figuras geométricas")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Rombo")
    print("6. Trapecio")
    print("0. Salir")

    opcion = int(input("Seleccione una opción: "))

    while opcion != 0:
        if opcion == 1:
            lado = float(input("Ingrese el lado: "))
            area = lado * lado
            print("El área del cuadrado es:", area)
        elif opcion == 2:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = base * altura
            print("El área del rectángulo es:", area)
        elif opcion == 3:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = (base * altura) / 2
            print("El área del triángulo es:", area)
        elif opcion == 4:
            radio = float(input("Ingrese el radio: "))
            area = 3.14159 * (radio * radio)
            print("El área del círculo es:", area)
        elif opcion == 5:
            d1 = float(input("Ingrese el primer diámetro: "))
            d2 = float(input("Ingrese el segundo diámetro: "))
            area = (d1 * d2) / 2
            print("El área del rombo es:", area)
        elif opcion == 6:
            base1 = float(input("Ingrese la base superior: "))
            base2 = float(input("Ingrese la base inferior: "))
            altura = float(input("Ingrese la altura: "))
            area = (base1 + base2) * altura / 2
            print("El área del trapecio es:", area)
        else:
            print("Opción inválida.")

        print("\nCálculo de áreas de figuras geométricas")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Círculo")
        print("5. Rombo")
        print("6. Trapecio")
        print("0. Salir")

        opcion = int(input("Seleccione una opción: "))

if __name__ == "__main__":
    main()