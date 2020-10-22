import random
from time import sleep
list=[1,2,3,4,5]
seq = random.choice(list)
num = int(input('Vou pensar em um número de 0 a 5. Tente advinhar: '))
print('PROCESSANDO...')
sleep(2)
if num == seq:
    print('Parabens! você acertou.')
    print('Nós pensamos no {num} ')
else:
    print('Continue tentando!')
    print(f'O número que eu pensei foi {seq} e você no {num}')

