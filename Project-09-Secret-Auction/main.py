# Store the name of auction participant and bid amount in list inside dictionary

auction = {}

# Ask the participant of their name and bid amount.
# .strip() compromise the mistaken spaces and .title() convert the first letter to capital.
# I will use while loop here because I don't know the number of participant

while True:

    # Name Input
    while True:
        participant = input("Enter your name: ").strip().title()
        if not participant:
            print("For identification you need to enter your name!")
        elif participant in auction:
            print("You are already in the list.")
        else:
            break

    # Bid Input
    while True:
        bid_amount = input("Enter your bid in $: ")
        if not bid_amount.isdigit():
            print("Enter amount in numbers.")
        else:
            bid_amount = int(bid_amount)
            break

    # Store the data into dictionary
    auction[participant] = bid_amount
    print("Bid added successfully!\n")

    # Asking user to add more bidder or exit
    more_bid = input("You wanna add more bidder 'yes' or 'no'")
    if more_bid.lower() != "yes":
        break


# to get the winner
highest_bid = 0
winner = ""

for name in auction:
    if auction[name] > highest_bid:
        highest_bid = auction[name]
        winner = name
print(f"The winner is {winner} with ${highest_bid} bid.")
