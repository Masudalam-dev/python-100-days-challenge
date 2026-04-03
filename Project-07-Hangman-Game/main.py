import random
from word_list import medium_word
from hangman_logo import logo
import hangman_art

print("WELCOME TO HANGMAN GAME!")
print(logo)



lives = 6
chosen_word = random.choice(medium_word)

print("Hint: It's a Fruit Name.")

word_length = len(chosen_word)
display = "_" * word_length
print(display)

store_letter = []
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in store_letter:
        print("You already guessed that letter.")
        continue

    store_letter.append(guess)

    new_display = ""

    for letter in chosen_word:
        if letter in store_letter:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("You have", lives, "lives left.")

    if lives == 0:
        print("You lose the Game.")
        game_over = True

    if "_" not in display:
        print("You won the Game.")
        game_over = True


    print(hangman_art.stages[lives])