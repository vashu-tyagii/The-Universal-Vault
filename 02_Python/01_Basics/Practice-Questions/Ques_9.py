year = int(input(' Enter year to check Leap Year : '))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"This year is leap year : {year}")
else:
    print(f"This year is not leap year : {year}")