# Store the name of auction participant and bid amount in list inside dictionary
auction = {
    "names": [],
    "bid_values": []
}

# Ask the participant of their name and bid amount.
# .strip() compromise the mistaken spaces and .title() convert the first letter to capital.
# I will use while loop here because I don't know the number of participant
condition = True
while condition:
    while condition:
        participant_name = input("Enter your name: ").strip().title()
        if not participant_name:
            print("For identification you need to enter your name!")
        elif participant_name in auction:
            print("You are already in the list.")
        else:
            break

    while condition:
        bid_amount = input("Enter your bid in $: ").isdigit()
        if bid_amount:
            print("Added")
            break
        else:
            print("Enter amount in numbers.")

    more_bid = input("You want add more bidder 'yes' or 'no'")
    if more_bid.lower() != "yes":
        break


