altura= float(input('qual sua altura?'))
peso= float(input('qual o seu peso?'))
imc= peso /(altura/100)**2

if imc < 18.5:
    print('magreza')

elif imc >=18.5 and imc < 24.9:
    print ('normal')

elif imc >=25.0 and imc < 29.9:
    print('sobrepesp')

elif imc >= 30.0 and imc < 39.9:
    print ('obesidade')

else:
    print('obesidade GRAVE')