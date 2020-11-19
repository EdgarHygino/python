'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o
tempo que falta ou que passou do prazo.'''

from datetime import date

nasc = int(input('Qual seu ano de nascimento: '))
idade = date.today().year-nasc
if idade < 18:
    print(f'Ainda não é hora do alistamento falta {18-idade} anos para seu alistamento')
    print(f'Voce deve se alistar em {date.today().year+(18-idade)}')
elif idade == 18:
    print(f'Você tem {idade} anos e esta na hora de seu alistamento')
else:
    print(f'Você passou {idade-18} do prazo de alistamento')