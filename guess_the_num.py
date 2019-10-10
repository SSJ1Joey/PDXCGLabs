import random

print("Welcome to guess the number! I'm sorry you're bored...\n")


nums = ('1','2','3','4','5','6','7','8','9','10')

def game():
    while True:
        print('Try and guess what number im guessing... between 1 and 10: ' )
        user_choice = input()
        attempts = 0
        comp_choice = random.choice(nums)
        if user_choice == comp_choice:
            print('You guessed correct!')
            break
        elif user_choice < comp_choice:
            print("You're too low...")
            attempts += 1 
            print('Attempts:',attempts)
        else:
            print("You're too high...")
            attempts += 1
            print('Attempts:',attempts)

game()

    


