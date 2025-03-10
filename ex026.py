frase = str(input('Digite qualquer frase: ')).upper().strip()
print("Nesta frase temos a letra 'A' {}x".format(frase.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('E aparece por ultimo na posição {}'. format(frase.rfind('A')+1))