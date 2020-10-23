#Duas formas de calcular media.

def media():
    nota1 = int(input('Digite sua nota: '))
    nota2 = int(input('Digite sua segunda nota: '))
    nota3 = int(input('Digite sua terceira nota: '))
    nota4 = int(input('Digite sua quarta nota '))
    while (nota1 + nota2 + nota3 + nota4) / 4 >= 7:
        print('Aluno Aprovado')
        break
    if (nota1 + nota2 + nota3 + nota4) / 4 < 7:
        print('Aluno reprovado')

media()

print('-------'* 100)

# Segundo modelo para calcular as médias usando funções

def valorLista():
    for i in range(1, 5):
        lista.append(int(input(f'Digite o valor da sua prova {i}: ')))


def valorMedia():
    s = 0
    for i in range(len(lista)):
        s = s + lista[i]
    m = s / 4
    return m

def resp():
    if m >= 7:
        print(f'Aluno aprovado com nota {m} ')
    else:
        print(f'Aluno reprovado com nota {m}')


lista = []
valorLista()
m = valorMedia()
resp()


