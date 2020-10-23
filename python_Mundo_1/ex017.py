import math

catop = float(input('Digite o temanho do cateto oposto: '))
cataj = float(input('Digite o tamanho do cateto adjacente: '))

reship = ((catop ** 2 ) + ( cataj ** 2)) ** 0.5

print('A hipotenusa vai medir {:.2f} '.format(reship))
# outro jeito de calcular usando uma biblioteca
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(catop,cataj)))

