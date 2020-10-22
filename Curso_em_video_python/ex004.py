var = input("Digite algo: ")

print(f'O tipo primitivo desse valor é {type(var)}')
print('Só tem espaço? ', var.isspace())
print(f'É um número? ', var.isnumeric())
print(f'É alfabético? {var.isalpha()}')
print('É alfanúmerico? ', var.isalnum())
print(f'Esta tudo em Maiúscula? {var.isupper()}')
print(f'Está em minúsculas? {var.islower()}')
print(f'Está capitalizada? {var.istitle()}')




