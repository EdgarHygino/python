lista=[]
while True:
    lista.append(int(input('Digite um número que queira consultar a tabuada: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('_' * 20)

print(f'Você quer consultar a tabuada de {len(lista)} números')
lista.sort()
print(f'Os números digitados são: {lista}')

for i in range(len(lista)):
    for l in range(1, 11):
        print('{} x {:2} = {:2} '.format(lista[i], l, lista[i] * l))
    print('_' * 20)
