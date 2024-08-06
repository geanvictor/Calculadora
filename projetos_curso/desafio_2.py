rend= int(input('qual o rendimento da tinta?'))
alt= int(input('qual a altura da parede?'))
lar=int(input('qual a largura da parede?'))

def rendimento():
    metro=alt*lar
    total=metro/rend
    print('a parede tem',metro,'metros quadrados')
    print('o rendimento da lata de tinta é de',total,'metros quadrados') 
    
rendimento()