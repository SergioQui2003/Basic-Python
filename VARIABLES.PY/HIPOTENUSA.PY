# para poder hallar la hipotenusa necesitamos saber los catetos de cada una por ello de bebemos preguntar a la persona cuales requieren 
import math

a = float(input("Ingrese el valor de un cateto: "))
b = float(input("Ingrese el valor del otro cateto: "))

c = math.sqrt(a**2 + b**2)
# aqui vamos hallar la hipotenusa según los datos dados 
print("La hipotenusa es:", c )