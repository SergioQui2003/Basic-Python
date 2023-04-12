IMC = peso / (talla * talla)

if IMC < 18.5:
    print("Bajo peso")
elif IMC >= 18.5 and IMC < 25:
    print("Peso normal")
elif IMC >= 25 and IMC < 30:
    print("Sobrepeso")
elif IMC >= 30 and IMC < 35:
    print("Obesidad moderada")
elif IMC >= 35 and IMC < 40:
    print("Obesidad severa")
else:
    print("Obesidad mórbida")