
class atm:
    
    def __init__(self, balance = 0, history = []):
        self.balance = balance
        self.history = history
       

    
    def check_balance(self):
        return self.balance

    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
        
    def check_withdrawal(self): 
        return self.balance >= self.withdraw
        

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
         

    def print_transactions(self):
        self.history.append(self.withdraw)
        self.history.append(self.deposit)
        print(self.history)

        



my_account = atm()
#my_account.deposit(15)
#print(my_account.check_balance())


while True:

    x = int(input('\n 1.Deposit \n 2.Withdraw \n 3.Check Balance \n 4.History \n 5.Exit \n Please select a number for service: '))
    if x == 1:
       my_account.deposit(int(input('How much would you like to deposit?: ')))
       print(f'Here is your balance: {my_account.check_balance()}')
    
    elif x == 2:
        my_account.withdraw(int(input('How much would you like to withdrawal?: ')))
        #my_account.check_withdrawal()
        print(f'Here is your balance: {my_account.check_balance()}')

    elif x == 3:
         print(f'Here is your balance: {my_account.check_balance()}')

    elif x == 4:
        print(my_account.print_transactions())

    else:
        print('Thank you come again!')
        break


        

    



