salario = float(input('Qual o salário atual? R$ '))

if salario <= 1250.00:
    salario += salario * 0.15
    print(f'Recebeu um aumento de 15% e passa a ganhar R${salario:.2f}')
else:
    salario += salario * 0.10
    print(f'Recebeu um aumento de 10% e passa a ganhar R${salario:.2f}')