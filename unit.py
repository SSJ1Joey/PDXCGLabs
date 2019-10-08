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
    unit = int(input('How many Meters want to convert to Meters?: '))
    print(f'You typed in {unit} Meters.')
    print(unit, ': Meters')

def kilometers():
    unit = int(input('How many Kilometers do you want to convert to Meters?: '))
    print(f'You typed in {unit} Kilometers.')
    print(unit * 1000, ': Meters' )
