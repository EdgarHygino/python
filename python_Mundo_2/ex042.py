'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

reta1 = float(input('Qual o tamanho da primeira reta? '))
reta2 = float(input('Qual o tamanho da segunda reta? '))
reta3 = float(input('Qual o tamanho da terceira reta? '))

if (reta1 - reta2) < reta3 < (reta1 + reta3) and (reta1 - reta3) < reta2 < (reta1 + reta3) and (reta3 - reta2) < reta1 < (reta3 + reta2):
    print('As retas podem formar um triangulo!')
    if reta1 == reta2 and reta3 == reta1:
        print('Esse é um triangulo EQUILÁTERO')
    elif reta1 == reta2 != reta3 or reta2 == reta3 != reta1 or reta3 == reta1 != reta2:
        print('Esse é um triangulo ISÓSCELES')
    else:
        print('Esse é um triangulo ESCALENO')
else:
    print('As retas não podem formar um tringulo!')
