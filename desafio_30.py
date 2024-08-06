num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))

mult = lambda num1, num2 : num1 * num2

print(f'o valor da multiplicação entre {num1} e {num2} é {mult(num1,num2)}')