import math

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = math.floor(len(lista) - 1)

    while baixo <= alto:
        meio = math.floor((baixo + alto) / 2)
        chute = lista[meio]

        if chute == item:
            return meio 

        if chute > item:
            alto = meio - 1

        else:
            baixo = meio + 1

    return None

print(pesquisa_binaria([1, 2, 3, 4, 5], 2))


