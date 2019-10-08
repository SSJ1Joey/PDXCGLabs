print('Lets make some change!')

def main():
    amount = int(input('Please enter an amount in cents: '))
    print(amount // 100, 'Dollars')
    amount = amount % 100
    print(amount // 25, 'Quarters')
    amount = amount % 25
    print(amount // 10, 'Dimes')
    amount = amount % 10
    print(amount // 5, 'Nickles')
    amount = amount % 5
    print(amount // 1, 'Pennies')
    amount = amount % 1

main()
