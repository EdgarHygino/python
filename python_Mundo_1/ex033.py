pri = int(input('Digite o primeiro número: '))
seg = int(input('digite o segundo número: '))
ter = int(input('Digite o terceiro número: '))

def maior (pri, seg, ter):
    upper = [pri, seg, ter]
    upper.sort()
    up = upper[2]
    return up

def menor (pri, seg, ter):
    lower = [pri, seg, ter]
    lower.sort()
    dow = lower[0]
    return dow

up = maior(pri, seg, ter)
dow = menor(pri, seg, ter)

print(f'O maior numero é {up}')
print(f'O menor numero é {dow}')
