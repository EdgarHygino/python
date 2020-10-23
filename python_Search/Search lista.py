#Busca sequencial desordenada
def busca_sequencial(lista, elemento):
    pos = 0
    encontrado = False

    while pos < len(lista) and not encontrado:
        if lista[pos] == elemento:
            encontrado = True
        else:
            pos = pos + 1
    return encontrado


testelista = ['edgar', 'dalva', 'arthur', 3, 10, 20, 'ariete']
print(busca_sequencial(testelista, 'ariete'))
print(busca_sequencial(testelista, 20))
