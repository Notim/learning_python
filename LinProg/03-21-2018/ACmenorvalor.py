num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

if (num1 == num2 and num1 == num3):
    print("todos od valores sao iguais")

else:
    if (num1 < num2 and num1 < num3):
        print("o menor numero eh {}".format(num1))
    else:
        if(num2 < num3 and num2 < num1):
            print("o menor valor eh {}".format(num2))
        else:
            if(num3 < num2 and num3 < num1):
                print("menor valor eh {}".format(num3))
            else:
                print("nao existe menor valor")
