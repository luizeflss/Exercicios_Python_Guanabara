from math import hypot
num1 = float(input('digite o valor do cateto oposto do triangulo: '))
num2 = float(input('Agora digite o valor do cateto adjacente: '))
h = hypot(num1, num2)
print('O comprimento da hipotenusa é igual á: {:.2f}'.format(h))