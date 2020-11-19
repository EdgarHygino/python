'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
from datetime import date

nasc = int(input('Qual seu ano de nascimento: '))
idade = date.today().year-nasc
if idade <= 9:
    print(f'Aluno tem {idade} anos e sua categoria é Mirim')
elif idade <= 14:
    print(f'Aluno tem {idade} anos e sua categoria é Infantil')
elif idade <= 19:
    print(f'Aluno tem {idade} anos e sua categoria é Junior')
elif idade <= 25:
    print(f'Aluno tem {idade} anos e sua categoria é Senior')
else:
    print(f'Aluno tem {idade} anos e sua categoria é Master')