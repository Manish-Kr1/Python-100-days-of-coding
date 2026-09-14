year = int(input("enter a year "))

if (year % 100 == 0) & (year % 400 == 0):
    print(year, "is leap year ")

elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year ")

else:
    print(year, "is not a leap year ")

