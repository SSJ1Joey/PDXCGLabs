import random

def comp_ticket():
    luck = range(1, 20)
    numbers = []
    for i in range(6):
        numbers.append(random.choice(luck))
    return numbers

def user_ticket():
    luck = range(1, 20)
    numbers = []
    for i in range(6):
        numbers.append(random.choice(luck))
    return numbers
    
def matches(user_ticket):
    comp_pick = user_ticket
    user_pick = user_ticket

    #print(comp_pick)
    #print(user_pick)

    matches = 0
    for i in range(len(comp_pick)):
        if comp_pick[i] == user_pick[i]:
            matches += 1
    return matches

def balance(matches):
    if matches == 1:
        balance += 4
    elif matches == 2:
        balance += 7
    elif matches == 3:
        balance += 100
    elif matches == 4:
        balance += 50000
    elif matches == 5:
        balance += 1000000
    elif matches == 6:
        balance += 25000000

    return balance 


def game(balance):
    for i in range(100000):
        ticket(balance)
    print(balance)
    

    
game(balance(matches(user_ticket())))
  







 
   

