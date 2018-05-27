#joao vitor aulino martins
#locacao carro


distancia = float(input("Digite a qtd de KM rodados: "));
dias = int(input("qtd de dias de locacao: "));
precoDias = (60 * dias);
precoKM = (0.15 * distancia);
precoTotal = (precoDias + precoKM);
print("O preco total é: R$",round(precoTotal,2));
input("press any key to continue...");
