#codigo feito apenas com meu breve conhecimento da linguagem.
numero = str(input('Digite um número de 0 a 9999: ')).strip()
num = int(numero)

if 0 <= num <= 9:
    unidade = numero[0]
    print('Este número possui: \n'
      '{} UNIDADE(S) = {}\n'. format(unidade, unidade))

if 10 == num:
    dezena = numero[0]
    print('Este número possui: \n'
          '{} DEZENA(S) = {}\n'.format(dezena, dezena))

if 10 < num <= 99:
    unidade = numero[1]
    dezena = numero[0]
    print('Este número possui: \n'
      '{} UNIDADE(S) = {}\n'
      '{} DEZENA(S) = {} \n' . format(unidade, unidade, dezena, dezena + '0'))

if 100 == num:
    centena = numero[0]
    print('Este número possui: \n'
          '{} CENTENA(S) = {}\n'.format(centena, centena + '00'))

if 100 < num <= 999:
    unidade = numero[2]
    dezena = numero[1]
    centena = numero[0]
    print('Este número possui: \n'
      '{} UNIDADE(S) = {}\n'
      '{} DEZENA(S) = {} \n'
      '{} CENTENA(S) = {} \n'
          .format(unidade, unidade, dezena, dezena + '0', centena, centena + '00'))

if 1000 == num:
    milhar = numero[0]
    print('Este número possui: \n'
          '{} MILHAR(ES) = {}\n'.format(milhar, milhar))

if 1000 < num <= 9999:
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]
    print('Este número possui: \n'
      '{} UNIDADE(S) = {}\n'
      '{} DEZENA(S) = {} \n'
      '{} CENTENA(S) = {} \n'
      '{} MILHAR(ES) = {}'
          .format(unidade, unidade, dezena, dezena + '0', centena, centena + '00', milhar, milhar + '000'))
