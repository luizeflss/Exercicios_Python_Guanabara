from random import choice
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
als = [al1, al2, al3, al4]
answer = choice(als)

print('{} é o escolhido para apagar o quadro.'.format(answer))