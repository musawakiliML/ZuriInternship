# Simple CLI Calculator

operations = "1. Addition 2. Subtraction 3. Division 4. Multiplication 5. Modulus"
user_choice = input(f"Enter a Choice:\n {operations}\n")

number_1 = eval(input("Enter Number 1:"))
number_2 = eval(input("Enter Number 2:"))

if user_choice == '1':
    addition = number_1 + number_2
    print(f"The Result of {number_1} + {number_2} is:{addition}")
elif user_choice == '2':
    subtraction = number_1 - number_2
    print(f"The Result of {number_1} - {number_2} is:{subtraction}")
elif user_choice == '3':
    division = number_1 / number_2
    print(f"The Result of {number_1} / {number_2} is:{division}")
elif user_choice == '4':
    multiplication = number_1 * number_2
    print(f"The Result of {number_1} * {number_2} is:{multiplication}")
elif user_choice == '5':
    modulus = number_1 % number_2
    print(f"The Result of {number_1} % {number_2} is:{modulus}")
else:
    print("Invalid Choice. Try Again!")
