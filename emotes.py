import random

print('Welcome! Looks like you could use a new face!\n')

eyes = [':', '8', '=', ';', 'X']
nose = ['o', '-', '0', 'V', '3']
mouth = [')', 'D', ']', '(', 'o']

while True:
    print('Would you like to see a face? yes/no')
    answer = input()
    if answer == 'yes':
        print(f'Much better! {random.choice(eyes)}{random.choice(nose)}{random.choice(mouth)}')
    else:
        print('Thanks for playing!')
        break
