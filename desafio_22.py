cidades_capitais={'são paulo': 'são paulo', 'rio de janeiro':'rio de janeiro', 'pernambuco':'recife'}

cidade = str(input('digite uma cidade:'))

if cidade in cidades_capitais:
    print('a capital de',cidade,'é', cidades_capitais[cidade])
else:
    print('nao')
    