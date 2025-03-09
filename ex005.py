n1 = int(input('Digite um número inteiro: '))
suss = int(n1+1)
ant = int(n1-1)
print('O sucessor deste número é {}, e o antecessor é {}.'.format(suss, ant))
print('')

#ou entao pode ser feito utilizando apenas uma variavel, veja abaixo:
n1 = int(input('Digite um número inteiro: '))
print('O sucessor deste número é {}, e o antecessor é {}.'.format((n1 + 1), (n1 - 1)))

#Porem, ao fazer dessa forma eu perco a possibilidade se utilizar as variaveis ant e sucess mais pra frente !!!!

