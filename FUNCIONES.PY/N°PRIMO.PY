def es_primo(numero):
    if numero <= 1:
        return False

    # Comprobar si hay un divisor desde 2 hasta num-1
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True
numero = 17
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")