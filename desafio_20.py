#numeros = [1,2,3,4,5,6,7,8,9,10]
# posso tambem fazer uma lista que CRIE uma lista de numeros em um determinado range
numeros = list(range(1,11))


for numero in numeros:
    if numero % 2== 0:
        print('o numero',numero,' é par')
    else:
        print('o numero',numero,' é ímpar')
        