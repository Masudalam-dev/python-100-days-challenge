
def is_leap_year(year):
    if ( year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Loop Year!")
    else:
        print("Not a loop Year!")

is_leap_year(2100)