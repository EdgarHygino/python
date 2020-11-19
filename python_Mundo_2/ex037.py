'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal e
3 para hexadecimal.'''


number = int(input('Didite um número inteiro: '))

opcoes = float(input('''Escolha os numeros de 1 a 3:
# [ 1 ] converter para BINÁRIO
# [ 2 ] converter para OCTAL
# [ 3 ] converter para HEXADECIMAL '''))
if opcoes == 1:
    print(f'O numero {number} em binario é {bin(number) [2:]}')
elif opcoes == 2:
    print(f'O numero {number} em octal é {oct(number)[2:]}')
elif opcoes == 3:
    print(f'O numero {number} em hexadecimal é {hex(number)[2:]}')
else:
    print('Opção invalida tente novamente! ')


#Outra forma de gerar condições usando array

def opcao1():
   binario = bin(number)
   print(f'O numero {number} em binario é {binario [2:]}')

def opcao2():
    octal = oct(number)
    print(f'O numero {number} em binario é {octal[2:]}')

def opcao3():
    hexa = hex(number)
    print(f'O numero {number} em binario é {hexa[2:]}')


opcoes = {1:opcao1, 2:opcao2, 3:opcao3}

opcoes.get(float(input('''Escolha os numeros de 1 a 3:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')))()


