nome = input('Digite seu nome completo: ')

nome1 = nome.split()
print(f'Seu Primeiro nome é: {nome1[0].capitalize()}')
print(f'Seu ultimo nome é:  {nome1[-1].capitalize()}')
meio = int(len(nome1) / 2)
print(f'Seu nome do meio é: {nome1[meio]}')