import random
# Rock Paper and Scissors Game

# Winning a Round:
# Rock defeats Scissors.
# Scissors defeat Paper.
# Paper defeats Rock.
# If gesture is same it's draw like Rock and Rock

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


print("Welcome to Rock, paper and Scissors Game")
game_items =[rock,scissors,paper]

user_input_num = int(input("What you wanna choose : 0 for Rock:  1 for Scissors:  and 2 for Paper: "))
user_choose = game_items[user_input_num]

computer_index_value = random.randint(0,2)
computer_choose = game_items[computer_index_value]


if user_choose == computer_choose:
    print(f"You choose: {user_choose}\nComputer Choose: {computer_choose}\nIt's draw 🤝.")
elif user_choose == rock and computer_choose == scissors:
    print(f"You Choose: {user_choose}\nComputer Choose: {computer_choose}\nYou win the Game 🏆🥇👑.")
elif user_choose == scissors and computer_choose == rock:
    print(f"You Choose: {user_choose}\nComputer Choose: {computer_choose}\nComputer win the Game.")
elif user_choose == scissors and computer_choose == paper:
    print(f"You Choose: {user_choose}\nComputer Choose: {computer_choose}\nYou win the Game 🏆🥇👑.")
elif user_choose == paper and computer_choose == scissors:
    print(f"You Choose: {user_choose}\nComputer Choose: {computer_choose}\nComputer win the Game.")
elif user_choose == paper and computer_choose == rock:
    print(f"You Choose: {user_choose}\nComputer Choose: {computer_choose}\nYou win the Game 🏆🥇👑.")
elif user_choose == rock and computer_choose == paper:
    print(f"You Choose: {user_choose}\nComputer Choose: {computer_choose}\nComputer win the Game.")
