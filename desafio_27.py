def fatoracao(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatoracao(n - 1)
numero =int(input('digite um numero:'))
print (f'O resultado de{numero} é {fatoracao(numero)}')