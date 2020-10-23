salario = float(input('Qual o sálario do funcionário? R$ '))
aumento = 0.15
novosal = salario + salario * aumento
print('Um funcionario que ganhava R${}, com 15% de aumento, passa a receber R${:.2f} '.format(salario, novosal))
