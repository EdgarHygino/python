dia = float(input('Quantos dias alugado? '))
km = float(input('Quantos KM rodados? '))
total = (60*dia)+(km*.15)
print('O total a pagar é de R${:.2f}'.format(total))