import random

options = ["R", "P", "S"]
# to get the desired output of Player(Rock) : CPU(Paper)
options_selection = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissor'}
computer_input = random.choice(options)
print(computer_input)
flag = True
user_input = input("Pick an Option:('R', 'P' or 'S')")

while flag:
    while user_input not in options:
        print("Error: Invalid Input Try Again:")
        user_input = input()

    #computer_input = random.choice(options)

    print(
        f"Player ({options_selection[user_input]}):CPU ({options_selection[computer_input]})")

    if user_input == computer_input:
        print(f"Both Selected Move {user_input}, It's a Tie!!")
        break
    elif user_input == 'R':
        if computer_input == 'S':
            print("Rock beats Scissors! Player(You) win!")
        else:
            print("Paper beats Rock! Computer(CPU) win!")

        flag = False
    elif user_input == 'P':
        if computer_input == 'R':
            print("Paper beats Rock! Player(You) win!")
        else:
            print("Scissors beats Paper! Computer(CPU) win!")

        flag = False

    elif user_input == 'S':
        if computer_input == 'P':
            print("Scissors beats Paper! Player(You) win!")
        else:
            print("Rock beats scissors! Computer(CPU) win!")
        flag = False
