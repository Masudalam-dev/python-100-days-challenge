print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))

tip_amount = (bill * tip) / 100
total_bill_amount = tip_amount + bill
split_the_bill = total_bill_amount / people

each_to_pay = round(split_the_bill , 2)
print(f"Each should pay: ${each_to_pay}")
