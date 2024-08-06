cidades = ('são paulo','rio de janeiro','salvador')
cidade= input('digite o nome de uma cidade:')

if cidade.lower() in cidades:
    print('acertou')
else:
    print('Esta cidade não esta na lista')
