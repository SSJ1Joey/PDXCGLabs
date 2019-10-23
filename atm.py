
class atm:
    
    def __init__(self, balance = 0):
        self.balance = balance
       

    
    def check_balance(self):
        return self.balance

    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
        
    def check_withdrawal(self): 
        return self.balance >= withdrawal
        

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
         

    def print_transactions():
        pass



my_acc = atm()
my_acc.deposit(15)
print(my_acc.check_balance())