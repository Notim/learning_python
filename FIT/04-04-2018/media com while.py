x = 0
contador = 0
print("Digite valores para somar a media no final: ")
while contador <= 10:
    contador += 1
    x += int(input("Digite um valor para adicionar a media: "))
    print("Notas faltantes: ", (10 - contador))

print("Media total: ", (x / contador))


