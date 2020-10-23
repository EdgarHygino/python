# iniciei com 3 aspas como se fosse um comentário
'''nome = str(input('Qualé o seu nome? ')).title().strip()
if nome == 'Edgar':
    print('Que nome legal que você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}')'''# fechando o comentário / python interpreta como string e não toma ação

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {float(m)}')
if m >= 6.0:
    print('Sua média foi boa! Não fez mais que sua obrigação!')
else:
    print('Sua média foi horrivel! começe a estudar o mais breve possivel!')

#condição simplificada
print('Parabens!' if m >= 6 else 'Estude mais!')

