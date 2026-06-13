from random import randint

random_number = randint(1, 100)

lives = 5

while lives > 0:
    user_number = int(input("Enter a number between 1 and 100: "))

    if user_number == random_number:
        print("You won!")
        break

    elif user_number < random_number:
        lives -= 1
        print("The random number is greater.")
        print(f"You have {lives} lives left.")

    else:
        lives -= 1
        print("The random number is smaller.")
        print(f"You have {lives} lives left.")

else:
    print("You lost!")
    print(f"The number was {random_number}")

print("Game over")