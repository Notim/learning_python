import random


def orderToMenor (a, b, c):
    array = [a, b, c]
    array = sorted(array)
    return array[0]


def criarLista(a):
    lista = []

    for i in range(0, a):
        lista.append(random.randrange(0, 100))


    return lista


def ordenarListas(vetor1, vetor2, vetor3):
    listaFinal = []

    for i in range(0, len(vetor1)):
        menorValor = orderToMenor(vetor1[i], vetor2[i], vetor3[i])
        listaFinal.append(menorValor)

    return listaFinal


vetor1 = criarLista(5)
vetor2 = criarLista(5)
vetor3 = criarLista(5)

print(vetor1)
print(vetor2)
print(vetor3)

print(ordenarListas(vetor1, vetor2, vetor3))