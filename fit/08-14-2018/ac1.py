#-----------------------------------#
# AC1 - Linguagem de Programação II
# João vitor paulino
# Ra: 1801021
#-----------------------------------#

# 1 - Dados como parâmetros três letras,
# devolver um valor booleano indicando se
# todas são iguais
def compararLetras(letra1, letra2, letra3):
    if letra1 == letra2 :
        if letra2 == letra3 :

            return True

        return False

# 3 - Dada como parâmetro uma letra,
# retorne booleano se é uma consoante.
def consoante(letra):
    if(letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u"):
        return False

    return True

# 5 - Dado como parametro uma lista,
# retorne o inverso desta lista.
# (não use funções prontas - order, sort...).
def inverterLista(lista):
    listaInvertida = []

    j = 0
    for i in range((len(lista) - 1), -1, -1):
        listaInvertida.insert(j, lista[i])
        j = j + 1

    return listaInvertida

#7 - Dado como parametro uma lista,
#retorne a lista ordenada decrescente.
#(não use funções prontas - order, sort...).
def orderDesc(lista):
    #aplicação de bubble sort
    for j in range(len(list)-1, 0, -1):
        for i in range(j):
            if lista[i] > lista[i+1]:
                swap = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = swap

    #retorno com o metodo de inversão já existente
    return inverterLista(list)


#9 Dado como parametro 2 listas com numeros inteiros,
#retorne uma outra lista com o resto da divisão entre os respectivos
#índices de cada lista.
def  restodivisao (vetor1, vetor2):
    lista_valor_resto = []

    for i in range(0, len(vetor1)):
        lista_valor_resto.append(vetor1[i] % vetor2[i])

    return lista_valor_resto
