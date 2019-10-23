
class atm:
    
    def __init__(self, balance = 0, history = []):
        self.balance = balance
        self.history = history
       

    
    def check_balance(self):
        return self.balance

    
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f'You deposited ${amount}')
        return self.balance
        
        
    def check_withdrawal(self, amount): 
        if self.balance < amount:
            print('Sorry not enough funds...')
            return False
        

    def withdraw(self, amount):
        self.balance -= amount
        self.history.append(f'You withdrew ${amount}')
        return self.balance
         

    def print_transactions(self):
        print(self.history)

        



my_account = atm()
#my_account.deposit(15)
#print(my_account.check_balance())


while True:

    x = int(input('\n 1.Deposit \n 2.Withdraw \n 3.Check Balance \n 4.History \n 5.Exit \n Please select a number for service: '))
    if x == 1:
       my_account.deposit(int(input('How much would you like to deposit?: ')))
       print(f'Here is your balance: ${my_account.check_balance()}')
    
    elif x == 2:
        amount = int(input('How much would you like to withdrawal?: '))
        if my_account.check_withdrawal(amount) == False:
            continue
        else:
            my_account.withdraw(amount)
        print(f'Here is your balance: ${my_account.check_balance()}')

    elif x == 3:
         print(f'Here is your balance: ${my_account.check_balance()}')

    elif x == 4:
        my_account.print_transactions()

    else:
        print('Thank you come again!')
        break


        

    



