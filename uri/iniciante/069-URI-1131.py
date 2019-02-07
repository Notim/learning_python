def multi_13(str_values):

    values = str_values.split(" ")

    value1 = int(values[0])
    value2 = int(values[1])

    if value1 > value2:
        value1, value2 = value2, value1

    sum, x = 0, value1

    while x <= value2:
        if x % 13 != 0:
            sum += x
        x += 1

    return sum



print(multi_13(input()))