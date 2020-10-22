velocidade = int(input(" Qual é a velocidade atual do carro: "))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${float((velocidade - 80) * 7)}')

print('tenha um bom dia! Dirijá com segurança!')

