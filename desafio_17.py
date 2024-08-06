idade =  int(input('qual a sua idade?'))
if idade < 13:
    print('você é uma criança')
elif idade >= 13 and idade <= 19:
    print('você é adolecente')
else:
    print('boa sorte, agora você é um adulto')