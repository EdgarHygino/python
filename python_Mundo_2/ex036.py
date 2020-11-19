'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

home = float(input('Qual o valor da casa? '))
salary = float(input('Qual o seu salário? '))
time_pay = float(input('En quanto tempo pretende pagar o financiamento em anos? '))

time = time_pay*12
installment = home / time

print(f'O valor do imovel é de R${home:.2F}')
print(f'As parcelas serão de R$ {installment:.2F} para o período de {int(time)} meses, {int(time_pay)} anos')

if installment > (salary*.3):
    print('Infelismente seu salário não atinge o minimo de 30% para cobertura das parcelas')
    print('Financiamento não aprovado!')
else:
    print('Parabens você pode dar andamento ao seu financiamento')
    print('Financiamento Aprovado!')
