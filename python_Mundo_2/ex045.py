# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep

opcions = {0: 'PEDRA', 1: 'PAPEL', 2: 'TESOURA'}


def animation():
    print('{:^80}'.format('JO'))
    sleep(0.5)
    print('{:^80}'.format('KEN'))
    sleep(0.5)
    print('{:^80}'.format('PÔ!!!'))
    sleep(0.5)
    print('==' * 40)


def computer():
    seq = random.choice([0, 1, 2])
    return seq


gamer = 0

print('{:=^80}'.format('JOKENPÔ'))
while True:
    gamer = int(input('''Escolha
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA
    Qual é sua jogada? '''))
    animation()
    comp = computer()

    if gamer == 0:
        if comp == 0:
            print(f'Empate')
            print(f'Ambos jogaram {opcions.get(comp)}')
        elif comp == 1:
            print(f'Computador venceu {opcions.get(comp)}')
            print(f'você jogou {opcions.get(gamer)}')
        elif comp == 2:
            print(f'Jogador venceu {opcions.get(gamer)}')
            print(f'Computador jogou {opcions.get(comp)}')
    elif gamer == 1:
        if comp == 0:
            print(f'Jogador venceu {opcions.get(gamer)}')
            print(f'Computador jogou {opcions.get(comp)}')
        elif comp == 1:
            print(f'Empate')
            print(f'Ambos jogaram {opcions.get(comp)}')
        elif comp == 2:
            print(f'Computador venceu {opcions.get(comp)}')
            print(f'você jogou {opcions.get(gamer)}')
    elif gamer == 2:
        if comp == 0:
            print(f'Computador venceu {opcions.get(comp)}')
            print(f'você jogou {opcions.get(gamer)}')
        elif comp == 1:
            print(f'Jogador venceu {opcions.get(gamer)}')
            print(f'Computador jogou {opcions.get(comp)}')
        elif comp == 2:
            print(f'Empate')
            print(f'Ambos jogaram {opcions.get(comp)}')
    else:
        print('Opção invalida tente novamente')
        break
    print('=='*40+'\n')
print('===' * 40)
