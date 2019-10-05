def inputnum ():
    while True:
        number = input("enter number: ")
        if number.isnumeric():
            break
    return number


