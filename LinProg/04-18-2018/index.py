from binToDec import bin2dec
from divisores import *

print(bin2dec(int(input("Digite um numero binario para convercao: "))))

qtd = int(input("Digite um numero para descobrir quantos divisores ela tem: "))
print("O numero digitado tem " + str(qtdDiv(qtd)) + " divisores")

divi = int(input("Digite um numero para descobrir se e primo ou nao: "))

primo = verifPrimo(divi)
if primo:
    print("O numero e primo")
else:
    print("O numero nao e primo")

divPrimo = divPrimo(divi)

if divPrimo == True:
    print("O numero total ({}) de divisores do numero digitado e primo".format(qtdDiv(divi)))
else:
    print("O numero total ({}) de divisores do numero digitado NAO e primo".format(qtdDiv(divi)))