# Nested if else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))

if height >= 110:
    print("You can ride rollercoaster 😎 ")
    # Make sure you write age variable inside conditional statement otherwise it will work as global and also work for first else
    age = int(input("How old are you? "))
    gender = input("Your Gender: Male  Female  Others(Please write the first letter in Capital). ")
    if age < 12:
        if gender == "Male":
            print("You need to pay only 5$.")
        elif gender == "Female":
            print("You need to pay just $2.")
        else:
            print("You are Welcome!")
    elif age <= 18:
        print("You need to pay $8.")
    else:
        print("You need to pay $10.")

else:
    print("First Grow up BRO 😍")