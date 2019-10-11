import random

print('Welcome! Looks like you could use a new face!\n')

eyes = [':', '8', '=', ';', 'X']
nose = ['o', '-', '0', 'V', '3']
mouth = [')', 'D', ']', '(', 'o']

while True:
    print('Would you like to see a face? y/n')
    answer = input()
    if answer == 'y':
        for item in range(5):
            print(f'{random.choice(eyes)}{random.choice(nose)}{random.choice(mouth)}')
    else:
        print('Thanks for playing!')
        break
