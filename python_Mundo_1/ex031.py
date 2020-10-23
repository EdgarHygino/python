distancia = float(input('Qual é a distancia em Km da sua viagem: '))

if distancia > 200:
    print(f'O valor da sua passagem é de \33[1;31;43mR${distancia * .45:.2f}\33[m')
else:
    print(f'O valor da sua passagem é de \33[1;31;43mR${distancia * .50:.2f}\33[m')