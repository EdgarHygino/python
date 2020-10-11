produto = float(input('Qual o preço do produto? R$ '))
print('Para esse produto no valor R${}, na promoção com desconto de 5% vai custar R${:.2f} '.format(produto, produto-produto*.05))
