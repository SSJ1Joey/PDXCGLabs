import random

balance = 0


def pick_6():
    luck = range(1, 100)
    numbers = []
    for i in range(6):
        numbers.append(random.choice(luck))
    print(numbers)
    
def ticket():
    comp_ticket = pick_6()
    user_ticket = pick_6()

def game():
    single_win = comp_ticket[1] == user_ticket[1]

game()
    
    
    


  
