def bin2dec(bin):
    dec = 0
    base = 1
    while bin > 0:
        resto = bin % 10
        dec +=  resto * base
        base *= 2
        bin = bin// 10
    return dec