import random

print('Fight!\n')
print('*' * 9)

type = ['fire', 'water', 'grass']


wins = ['firegrass', 'waterfire', 'grasswater']

def game():
    while True:
        user_choice = input('Choose your type: [fire, water, grass] ').lower()
        comp_choice = random.choice(type)
        print(f'You chose: {user_choice} and I chose: {comp_choice}')
        if user_choice not in type:
            print('Please choose a valid option...')
        elif user_choice == comp_choice:
            print('Tie game')
        elif comp_choice in wins:
            print('You won!')
        else:
            print('You lost...')

game()

print('Would you like to play again? y/n')
answer = input()
if answer == 'y':
    game()
elif answer == 'n':
    quit()
