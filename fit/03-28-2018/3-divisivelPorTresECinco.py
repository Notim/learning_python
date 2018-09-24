verif = True

while verif:
    num = int(input("Digite qualquer valor: "))

    if((num % 5) == 0) and ((num % 3) == 0):
        verif = False
        print("Valor digitado eh divisivel por 5 e 3")