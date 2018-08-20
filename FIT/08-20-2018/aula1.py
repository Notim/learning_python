def main():
    start()


def addAddres(loop, funcao):
    dictionary = {}

    for index in range (loop):
        index = str(input("Digite um valor para " + funcao[0] + ": "))
        valor = str(input("Digite um valor para " + funcao[1] + ": "))

        dictionary[index] = valor

    return dictionary


def showDict(dict, funcao):
    print(funcao[0], " | ", funcao[1])
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