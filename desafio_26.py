def potencia(base,expoente=2):
    return base ** expoente

numero_base = int(input('digite o valor da base: '))
numero_expoente = input('digite o valor do expoente: ')

if numero_expoente:
    print(f'o resultado é:{potencia(numero_base, int(numero_expoente))}')
else:
    print (f'o resultado é:{potencia(numero_base)}')
    

    