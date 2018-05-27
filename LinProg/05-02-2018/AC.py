'''
Atividade Continua

----------------------------------
Nome : Joao vitor paulino martins
R.A. : 1801021
S.I. - 1ºD noturno
----------------------------------

Criar programa que receba numeros digitados pelo
usuario, enquanto a soma destes numeros for menor que 100
no final, imprima a soma total e a média '''


SUM = 0
CONT = 0

while SUM < 100:
       num = int(input("Digite um número: "))
       SUM += num
       CONT += 1
print("Média: ", SUM/CONT)

list = [10, 10, 10, 10, 10, 20, 30]


def sumList(lista):
    soma= 0
    for i in lista:
        soma += i
    return soma


#Criar uma função que retorne a média da soma de todos os
#valores de uma lista

def mediaList(soma):
    media = soma/len(list)
    return media


somalista = sumList(list)
medialista = mediaList(somalista)

print("Soma da lista: ", somalista)
print("Média da lista: ", round(medialista, 2))
