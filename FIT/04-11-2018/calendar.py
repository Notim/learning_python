year = int(input("Ano: "))
month = int(input("Mes: "))
bix = False


def verifbisext(rec):
    if(rec % 4 == 0) and (not (rec % 100 == 0) or (rec % 400 == 0)):
        print("O ano {} é bisexto !".format(rec))
        return True
    else:
        print("O ano {} nao é bisexto !".format(rec))
        return False


def verifValiddate(M,b):

    if (M > 12) or (M < 1):
        print("Mes invalido")
        exit()

    if M == 2:
        if b:
            print("O mes digitado tem 29 dias")
        else:
            print("O mes digitado tem 28 dias")

    elif (M == 1) or (M == 3) or (M == 5) or (M == 7) or (M == 8) or (M == 10) or (M == 12):
        print("O mes digitado tem 31 dias")
    elif (M == 4) or (M == 6) or (M == 9) or (M == 11):
        print("O mes digitado tem 30 dias")


def generatecalendar(b):
    i = 0
    print("-----------------------")
    while i < 13:
        i += 1
        if i == 2:
            if b == 1:
                print("O mes {} 29 dias".format(i))
            else:
                print("O mes {} 28 dias".format(i))

        elif (i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i == 12):
            print("O mes {} 31 dias".format(i))
        elif (i == 4) or (i == 6) or (i == 9) or (i == 11):
            print("O mes {} 30 dias".format(i))


def calen(m):
    days = 0
    while days < m:

        week = 0
        while week < 7:
            week += 1
            if days != m:
                days += 1
            else:
                break

            if days < 10:
                print(" {}".format(days), " ", end='')
            else:
                print("{}".format(days), " ", end='')

            #print("{0:0>2}".format(str(days)), " ", end = '')

        print(sep='\n')


def generatecalendarinformat(b):
    mes = 1
    while mes < 13:
        print("MES {}".format(mes))
        print(" D   S   T   Q   Q   S   S")

        # ----------------------------------------------#
        if mes == 2:
            if b:
                calen(29)
            else:
                calen(28)
        elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            calen(31)
        elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            calen(30)

        mes += 1
        #----------------------------------------------#

        print("--------------------------")
        print("")


bix = verifbisext(year)
verifValiddate(month, bix)
generatecalendar(bix)
generatecalendarinformat(bix)
generatecalendarinformat(bix)