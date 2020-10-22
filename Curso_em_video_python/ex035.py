reta1 = float(input('Qual o tamanho da primeira reta? '))
reta2 = float(input('Qual o tamanho da segunda reta? '))
reta3 = float(input('Qual o tamanho da terceira reta? '))
#caulculo retirado do site:  https://brasilescola.uol.com.br/matematica/triangulo.htm#:~:text=Para%20construir%20um%20tri%C3%A2ngulo%20n%C3%A3o,da%20diferen%C3%A7a%20entre%20essas%20medidas.

if (reta1 - reta2) < reta3 < (reta1 + reta3) and (reta1 - reta3) < reta2 < (reta1 + reta3) and (reta3 - reta2) < reta1 < (reta3 + reta2):
    print('As retas podem formar um triangulo!')
else:
    print('As retas não podem formar um tringulo!')
