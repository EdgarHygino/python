nome = input('Digite seu nome completo: ').strip()

nome = nome.upper()
search = False
if nome.find('SILVA') > 0:
    search = True

print('Seu nome tem Silva? {}'.format(search))
# ou pode ser feito assim:

print('Seu nome tem Silva? {}'.format('SILVA' in nome)) # muito mais pratico que minha idea