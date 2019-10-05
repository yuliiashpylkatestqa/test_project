from inputnum import inputnumber
def is_year_leap (year):

    if ((year % 4) != 0):
        return("No")
    else:
        if (year % 100 == 0) and (year % 400 != 0):
            print("No")
        else:
            return("Yes")
z=inputnumber()
r=is_year_leap(z)
print(r)