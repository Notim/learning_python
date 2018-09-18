year = input("Ano: ")
month = int(input("Mes: "))
bix = False

def toknowdaystart(month, bix):
    cen_digit = int(year[0] + year[1])
    year_digit = int(year[2] + year[3])
    incog = year_digit + (year_digit//4)

    if cen_digit == 18:
        incog += 2
    elif cen_digit == 20:
        incog += 6
    if month == 1 and bix == False:
        incog += 1
    elif month == 2 and bix == True:
        incog += 3
    elif month == 2 and bix == False:
        incog +=  4
    elif month == 3 or month == 11:
        incog += 4
    elif month == 4 or month == 7:
        incog += 0
    elif month == 5 :
        incog += 2
    elif month == 5:
        incog += 6


#verifica se o ano eh bisexto
def verifbisext(rec):
    if(rec % 4 == 0) and (not (rec % 100 == 0) or (rec % 400 == 0)):
        print("O ano {} é bisexto !".format(rec))
        return True
    else:
        print("O ano {} nao é bisexto !".format(rec))
        return False

#mostra o ultimo dia do mes
def showfinalday(M,b):

    if (M > 12) or (M < 1):
        print("Mes invalido")
        exit()

    if M == 2:
        if b:
            return 29
        else:
            return 28

    elif (M == 1) or (M == 3) or (M == 5) or (M == 7) or (M == 8) or (M == 10) or (M == 12):
        return 31
    elif (M == 4) or (M == 6) or (M == 9) or (M == 11):
        return 30

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

        print(sep='\n')

#envia os parametro de acordo com o dia final
def generatecalendarinformat(b):
    mes = 1
    while mes < 13:
        print("MES {}".format(mes))
        print("--------------------------")
        print(" D   S   T   Q   Q   S   S")

        calen(showfinalday(mes, b))

        mes += 1

        print("--------------------------")
        print("")


bix = verifbisext(int(year))
showfinalday(month, bix)
generatecalendarinformat(bix)