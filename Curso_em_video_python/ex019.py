import random
alunos = []
while True: # enquanto verdade
    alunos.append(input('Digite o nome do aluno ou OK para concluir: ')) #digite o nome
    if alunos[-1] in 'OKok': # se digitar OK ou ok o programa vai para break
        break # aqui encerra o looping do while
alunos.pop(-1) # aqui temos que tirar a palavra ok que foi implementada na lista que é a ultima posição por isso -1
for i in range(len(alunos)): # usando um for para imprimir em de forma crescento todos os nomes da lista
    print(f'Os alunos são {alunos[i]} ') # comando imprimir usando a chave gerada pelo looping do for na variavel i
print(f'O aluno escolhido é {random.choice(alunos)}') # usando a biblioteca random para e escolher uma posição da lista aleatoria

