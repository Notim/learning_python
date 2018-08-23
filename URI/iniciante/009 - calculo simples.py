valor = []
valor.append(input().split(" "))
valor.append(input().split(" "))

resultado = int(valor[0][1]) * float(valor[0][2])
resultado += int(valor[1][1]) * float(valor[1][2])

print("VALOR A PAGAR: R$ {0:.2f}".format(resultado))