var1 = int(input("Digite o primeiro numero: "))
var2 = int(input("Digite o segundo numero: "))

multi = var1 * var2

verif = multi % 2

if verif == 0:
    print("par ", multi)
else:
    print("impar ", multi)
