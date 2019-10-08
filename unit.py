print('Welcome to the unit converter.')

def foot():
    unit = int(input('How many Feet do you want to convert to Meters?: '))
    print(f'You typed in {unit} Feet.')
    print(unit *  0.3048, ': Meters' )

def mile():
    unit = int(input('How many Miles do you want to convert to Meters?: '))
    print(f'You typed in {unit} Miles.')
    print(unit * 1609.3, ': Miles')

def meter():
    unit = int(input('How many Meters do you want to convert to Meters?: '))
    print(f'You typed in {unit} Meters.')
    print(unit, ': Meters')

def kilometer():
    unit = int(input('How many Kilometers do you want to convert to Meters?: '))
    print(f'You typed in {unit} Kilometers.')
    print(unit * 1000, ': Meters' )

answer = input('What would you like to convert to Meters? (Feet, Miles, Meters or Kilometers)').lower()
if answer == 'feet':
    print(foot())
elif answer == 'miles':
    print(mile())
elif answer == 'meters':
    print(meters())
elif answer == 'kilometers':
    print(kilometer())
