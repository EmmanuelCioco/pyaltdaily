import random
computer_generated_number=random.randint(1,100)
user_guess_number=int(input("Guess the computer generated number from a range of 1-100:  "))
number_of_tries=1
while user_guess_number!=computer_generated_number:
    if user_guess_number>computer_generated_number:
        print("The number you guessed is high")
    elif user_guess_number< computer_generated_number:
        print("The number is low try again")
    elif abs(user_guess_number-computer_generated_number)<=10:
        print("You are close")
    elif abs(user_guess_number-computer_generated_number)<=5:
        print("You are very close")
    user_guess_number = int(input("Almost at it guess again: "))
    number_of_tries+=1
print(f"congratulations you guessed the computer generated number by {number_of_tries} times\n \nbye for now")