from datetime import date

years = int(input('Que ano quer analisar? ou digite 0 para analisar o ano atual: '))
if years == 0:
    years = date.today().year
if years % 4 == 0 and years % 100 != 0:
    print(f'O ano {years} é um ano bissexto')
else:
    print(f'O ano {years} Não é bissexto')