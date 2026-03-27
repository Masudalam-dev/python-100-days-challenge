print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
# small_pizza_pepperoni = 2
# medium_pizza_pepperoni = 3
# extra_cheese_for_any_size = 1

# instead of making all above variable we can do like this below 👇
pizza_price = 0

if size == "S":
    pizza_price = 15
elif size == "M":
    pizza_price = 20
elif size == "L":
    pizza_price = 25
if pepperoni == "Y" and size == "M":
    pizza_price += 2
elif pepperoni == "Y" and size == "L":
    pizza_price += 3
if extra_cheese == "Y":
    pizza_price += 1

print(f"Your final bill is: ${pizza_price}.")


# Another method to execute the code and this is better logic to visualize

if size == "S":
    pizza_price = 15
elif size == "M":
    pizza_price = 20
    if pepperoni == "Y":
        pizza_price += 2
elif size == "L":
    pizza_price = 25
    if pepperoni == "Y":
        pizza_price += 3
if extra_cheese == "Y":
    pizza_price += 1
print(f"Your final bill: ${pizza_price}")