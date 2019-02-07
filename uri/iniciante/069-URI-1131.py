def multi(str_values):

    values = str_values.split(" ")

    value1 = int(values[0])
    value2 = int(values[1])

    if value1 > value2:
        value1, value2 = value2, value1

    sum = 0

    for x in range(value1, value2):
        if x % 13 != 0 :
            sum += x


print(multi(input()))