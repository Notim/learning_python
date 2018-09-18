def tabuada():
    n = 0
    for n in range(11):
        j = 0
        for j in range(11):
            product = (j * n)
            file = open("archieve.txt", "+a")
            file.write(str(n)+" * "+ str(j) +" = "+str(product)+"\n")
            file.close()

        file = open("archieve.txt", "+a")
        file.write("--------------------------\n")
        file.close()

def par():
    file = open("sum.txt", "r")
    par = int(file.read())
    par = ((par % 2) == 0)
    file.close()

    if par:
        print("é par")
    else:
        print("é ímpar")


tabuada()
par()