'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''
import getpass

print('==='*15 + 'LOJA HYGINO' + '===' * 15)
value = float(input('Qual o valor total das compras R$: '))
payment = int(input('''Qual a forma de pagamento: 
[1]: à vista dinheiro/cheque: 10% de desconto
[2]: à vista no cartão: 5% de desconto
[3]: em até 2x no cartão: preço formal
[4]: 3x ou mais no cartão: 20% de juros'''))

if payment == 1:
    discount = value - value*.1
    print(f'\n A vista tem 10% e o valor fica em R$ {discount:.2f}')
elif payment == 2:
    discount = value - value*.05
    print(f'\n Aplicado o desconto de 5% e as compras tem o valor R$ {discount:.2f}')
elif payment == 3:
    discount = value
    print(f'\n O valor das compras é R${discount:.2f}')
else:
    discount = value + value * .20
    print(f'\n O valor para parcelamento 3x ou mais é de R$ {discount:.2f}')
