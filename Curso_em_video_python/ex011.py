largura = float(input("Digite quantos metros tem sua parede :"))
altura = float(input('Digite a largura da parede em metros: '))
m2 = largura * altura
tinta = .5
print('Sua parede tem a dimenssão de {}x{} e sua area é de {}mª.'.format(largura, altura, largura*altura))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(m2*tinta))