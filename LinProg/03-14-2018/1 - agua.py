#joao vitor paulino martins
#slario e agua

while True:
    print("__________________________");
    salario = float(input("Digite o salario minimo: "));
    consumo = float(input("Digite o consumo de agua: "));
    coeficiente = (0.02 * salario);
    precoAgua = coeficiente / 1000;
    precototal = consumo * precoAgua;
    print("O preco total é: " + str(round(precototal,2)))
    desconto = precototal * 0.15
    valorComDesconto = (precototal - desconto)
    print("O valor reduzido é: " + str(round(valorComDesconto,2)));
    if not (1):
        break
    
input("press any key to continue...");
