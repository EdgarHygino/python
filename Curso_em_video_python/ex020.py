import random
nome = []
while True:
    nome.append(input('Digite o nome do Aluno ou OK para completar: '))
    if nome[-1] in 'OKok':
        break
nome.pop(-1)
random.shuffle(nome) # usando a biblioteca ramdom para embaralhar a lista

print('A orden de apresentação será: ')
print(nome)
