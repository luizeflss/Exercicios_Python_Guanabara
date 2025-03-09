from math import sin, cos, tan, radians
angle = float(input('Digite o valor do ângulo: '))
coss = cos(radians(angle))
seno = sin(radians(angle))
tang = tan(radians(angle))
print('O ângulo {} possui aproximadamente os seguintes valores \n'
      'COS = {:.2f} \n'
      'SEN = {:.2f} \n'
      'TAN = {:.2f} '.format(angle, coss, seno, tang))