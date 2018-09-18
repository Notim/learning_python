def qtdDiv(n):
    div = 0
    i = 1
    while i<= n:
        if n % i == 0:
            div += 1
        i += 1

    return div

def verifPrimo(n):
    div = qtdDiv(n)
    if div == 2:
        return True
    if div > 2:
        return False


def divPrimo(primo):

    return(verifPrimo(qtdDiv(primo)))