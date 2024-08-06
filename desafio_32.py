lista = [1,2,3,4,5,6,7,8]
quadrado = lambda x :x ** 2 
resultado =[]

for x in lista:
    resultado.append(quadrado(x))
    
print (f'Os quadrados de{lista} são: {resultado}')