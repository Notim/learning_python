nome = str(input())
salariobruto  = float(input())
vendas  = float(input())
comissao = (vendas  * 0.15)
salariofinal = salariobruto + comissao

print("TOTAL = R$ {0:.2f}".format(salariofinal))
