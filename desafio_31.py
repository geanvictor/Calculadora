numero = int(input('digite um numero: '))

valor = lambda numero: 'par' if numero %2  == 0 else print('impar')
print(f'o numero é {valor(numero)}')