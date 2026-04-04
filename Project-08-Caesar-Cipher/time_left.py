print("Welcome to the reality check of time left in your life to do something now.")
user_age = int(input("HOW OLD ARE YOU:\n"))
def life_in_weeks(age):
    weeks_in_year = 52
    weeks_left = (90 * weeks_in_year) - (user_age * weeks_in_year)
    if age >= 90:
        print("You have already done a lot.\nNow it's time for rest.")
    else:
        print(f"You have {weeks_left} weeks left.")

life_in_weeks(user_age)