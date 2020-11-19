nome = str(input("Qual é o seu nome? "))
if nome == 'Edgar':
    print('Que nome bomito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil. ')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Seu nome é feminino')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}! ')
