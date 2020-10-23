lista=[]
while True:
    lista.append(int(input('Digite o número que quer consultar a tabuada 0')))
    teste = str(input('Quer saber mais alguma tabuada S/N ?'))
    if teste in 'nN':
        break
print('----Tabuada---'*30)

print(f'Voce quer consultar {len(lista)}  tabuadas')
lista.sort()
print(f'Essas tabuadas são dos {lista}')

for i in range(len(lista)):
    for l in range(1,11):
        print(f'{lista[i]} x {l} = {lista[i]*l}')
    print('---'*30)
