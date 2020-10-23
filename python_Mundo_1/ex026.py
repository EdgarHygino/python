frase = input('Digite uma frase: ').strip()

print(f'A letra A aparece {frase.upper().count("A")} vezez na frase')
print(f'A primeira letra A apareceu na posição {frase.upper().find("A")}')
print(f'A útima letra A apareceu na posição {frase.upper().rfind("A")}')