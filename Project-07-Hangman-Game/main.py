import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


store_letter = []
ori = 0
while ori < word_length:
    ori += 1
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            store_letter.append(letter)
        elif letter in store_letter:
            display += letter

        else:
            display += "_"
    print(display)

    if "_" not in display:
        print("You won the Game.")