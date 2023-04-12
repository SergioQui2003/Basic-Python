Import math

# Definir funciones para cada figura geométrica

def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return 0.5 * base * altura

def area_circulo(radio):
    return math.pi * radio ** 2

# Pedir al usuario que ingrese los datos necesarios para calcular las áreas1
figura = input("¿De qué figura geométrica quieres calcular el área? (cuadrado, rectángulo, triángulo, círculo) ")
if figura == "cuadrado":
    lado = float(input("Ingresa el valor del lado: "))
    print("El área del cuadrado es:", area_cuadrado(lado))
elif figura == "rectángulo":
    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))
    print("El área del rectángulo es:", area_rectangulo(base, altura))
elif figura == "triángulo":
    base = float(input("Ingresa el valor de la base: "))
    altura = float(input("Ingresa el valor de la altura: "))
    print("El área del triángulo es:", area_triangulo(base, altura))
elif figura == "círculo":
    radio = float(input("Ingresa el valor del radio: "))
    print("El área del círculo es:", area_circulo(radio))
else:
    print("La figura ingresada no es válida.")