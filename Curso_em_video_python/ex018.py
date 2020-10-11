import math
angulo = float(input("Digite o ângulo que deseja: "))
'''para usar a biblioteca math e calcular o seno, cosseno e tangente, 
precisamos converter o valor digitado de graus para radianos
formula padrão da biblioteca python. para isso usamos .radians()'''

seno = math.sin(math.radians(angulo))
cosseno = math.cos((math.radians(angulo)))
tangente = math.tan(math.radians(angulo))

print('O ângulo de {}º tem o SENO de {:.2F}'.format(angulo, seno))
print('O ângulo {}º tem o COSSENO de {:.2F}'.format(angulo, cosseno))
print('O angulo {}º tem a TANGENTE de {:.2F}'.format(angulo, tangente))

print('-----'*100)
#Ou podemos a formula diretamente no print sem precisar adicionar muitas variaveis
print('O ângulo de {}º tem o SENO de {:.2F}'.format(angulo, math.sin(math.radians(angulo))))
print('O ângulo {}º tem o COSSENO de {:.2F}'.format(angulo, math.cos(math.radians(angulo))))
print('O angulo {}º tem a TANGENTE de {:.2F}'.format(angulo, math.tan(math.radians(angulo))))
