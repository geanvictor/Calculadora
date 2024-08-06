funcionarios= ['ana','maecos','alice','pedro','sophia','bruno','melissa']
turno_dia = ['ana','marcos','alice','melissa']
turno_noite = ['pedro','sophia','bruno']
tem_carro = ['marcos','alice','bruno','melissa']

lista1= set(tem_carro).intersection(turno_noite)
print (lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)