def inputnumber():
    while True:
        number = input("enter number: ")
        if number.isnumeric():
            break
    return int(number)


