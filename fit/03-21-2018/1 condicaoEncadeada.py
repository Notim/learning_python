#condicoes encadeadas
nota = float(input("Digite a Nota: "));
auxiliar = float(input("Digite a Nota auxiliar: "));
if nota < 6.5:
    if(auxiliar > 6.5):
        print("Aluno Aprovado");
    else:
        print("Aluno Reprovado");
else:
    print("Aluno Aprovado");
