nome = str(input('Digite seu nome completo: '))
print('Aqui está o nome com cada modificação:')
print('CAPSLOCK:',(nome.upper()))
print('minúsculas:',(nome.lower()))
nospace = (nome.replace(" ",""))

print('Total letras s/espaços:', (len(nospace)))
nomel = (nome.split())

print('Total letras primeiro nome:', len(nomel[0]))