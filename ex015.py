km = float(input('Informe a distancia percorrida em KM: '))
days = int(input('Agora informe por quantos dias o veiculo foi alugado: '))
price = 60 * days + 0.15 * km
print('O custo total do aluguel deste veiculo é de R${}'.format(price))