def factorial(numero):
    if numero < 0:
        return None
    elif numero == 0:
        return 1
    else:
        fact = 1
        for i in range(1, numero+1):
            fact *= i
        return fact
numero = 5
factorial_de_n = factorial(numero)
print(factorial_de_n) # Imprime 120