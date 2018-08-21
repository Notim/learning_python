'''
Ac de linguagem de programação

João vitor paulino martins RA: 1801021
------------------------------------------------
Criar um cadastro de Funcionários por Nome e CPF.
O usuário deve digitar a quantidade de
funcionários que irá cadastrar,
depois deve perguntar se irá cadastrar por CPF
ou nome.
Se for por CPF, deve digitar a matricula e o CPF.
Se for por nome, deve digitar a Matricula e o Nome.
ao final,
imprimir a relação de funcionários cadastrados.
------------------------------------------------
'''

def main():
    start()


def addAddres(loop, funcao):
    dictionary = {}

    for index in range (loop):
        print("----------------------------")
        index = str(input("Digite um valor para " + funcao[0] + ": "))
        valor = str(input("Digite um valor para " + funcao[1] + ": "))

        dictionary[index] = valor

    return dictionary


def showDict(dict, funcao):
    print(funcao[0], " - ", funcao[1])
    for key in dict:
        print(key ," - ", dict[key])

def start():
    funcao = []
    print("Olá\n")

    funcao.append(str(input("Qual é o nome de chave: ")))
    funcao.append(str(input("Qual é o nome dos valores: ")))

    loop = int(input("Quantos cadastros deseja cadastrar: "))

    showDict(addAddres(loop, funcao),funcao)



main()