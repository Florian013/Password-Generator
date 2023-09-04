# Ask user if they want to generate a password or not
# If yes, ask for passwprd lenght
# Generate password
# Print password
# If initial response is no, exit the program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_lenght = int(input("How long do you want your password to be? "))
    random.shuffle(characters)
    password = []

    for i in range(password_lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


option = input("Do you want to generate a password? (Yes/No): ")
if option == "yes":
    generate_password()
elif option == "no":
    print("Program ended! ")
    quit()
else:
    print("Invalid input! ")