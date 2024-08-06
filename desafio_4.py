#um script que diga 'ola [nome] voce tem [anos] de idade
nome = str(input('digite seu some:'))
idade = int(input('digite sua iade:'))

print('Ola! {} voce tem {} anos de idade'.format(nome,idade))
#ou
print(f'Ola!,{nome},voce tem {idade} anos')