
import random

print("Select complexity: easy / medium / hard")
level = input("Select complexity:\t").lower()
attempts = 0
guesses = False

if level == "easy":
    print("You chose easy")
    print("You have 3 attempts")
    number = random.randint(1, 10)
    while attempts < 3:
        number2 = int(input("Enter number:\t"))
        if number == number2:
            print("Correctly")
            guesses = True
            break
        elif number > number2:
            print("More")
        else:
            print("Few")
        attempts = attempts + 1
    if not guesses:
        print('You lost! The correct number was ',number)

elif level == "medium":
    print("You chose medium")
    print("You have 5 attempts")
    number = random.randint(1, 50)
    while attempts < 5:
        number2 = int(input("Enter number:\t"))
        if number == number2:
            print("Correctly")
            guesses = True
            break
        elif number > number2:
            print("More")
        else:
            print("Few")
        attempts = attempts + 1

    if not guesses:
        print('You lost! The correct number was ',number)
elif level == "hard":
    print("You chose hard")
    print("You have 10 attempts")
    number = random.randint(1, 100)
    while attempts < 10:
        number2 = int(input("Enter number:\t"))
        if number == number2:
            print("Correctly")
            guesses = True
            break
        elif number > number2:
            print("More")
        elif number < number2:
            print("Few")
        else:
            print("")
        attempts = attempts + 1
    if not guesses:
        print('You lost! The correct number was ',number)

else:
    print("Invalid input")


