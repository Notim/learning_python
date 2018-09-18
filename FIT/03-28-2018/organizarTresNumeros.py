rev1 = int(input("Digite o primeiro valor: "))
rev2 = int(input("Digite o segundo valor: "))
rev3 = int(input("Digite o terceiro valor: "))

if (rev1 > rev2) and (rev1 > rev3):  # caso em que rev1 eh o maior
    print(rev1)
    if rev2 > rev3:  # rev1, rev2, rev3
        print(rev2)
        print(rev3)
    else:  # rev1, rev3, rev2
        print(rev3)
        print(rev2)
elif (rev2 > rev1) and (rev2 > rev3):  # caso em que o rev2 eh maior
    print(rev2)
    if rev1 > rev3:  # rev2, rev1, rev3
        print(rev1)
        print(rev3)
    else:  # rev2, rev3, rev1
        print(rev3)
        print(rev1)
elif (rev3 > rev1) and (rev3 > rev2):  # caso em que o rev3 eh maior
    print(rev3)
    if rev1 > rev2:  # rev3, rev1, rev2
        print(rev1)
        print(rev2)
    else:  # rev3, rev2, rev1
        print(rev2)
        print(rev1)
