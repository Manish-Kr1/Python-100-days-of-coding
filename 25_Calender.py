import calendar

year = int(input("enter a year: "))
month = int(input("Enter month in number: "))

calendar = calendar.month(year, month)
print(calendar)