import random

balance = 0


def pick_6():
    luck = range(1, 100)
    numbers = []
    first = random.choice(luck) 
    second = random.choice(luck) 
    third = random.choice(luck) 
    forth = random.choice(luck) 
    fifth = random.choice(luck) 
    sixth = random.choice(luck) 
    numbers.append(first)
    numbers.append(second)
    numbers.append(third)
    numbers.append(forth)
    numbers.append(fifth)
    numbers.append(sixth)
    
    
    

def ticket():
    pick_6()
    t_list = []
    for item in range(6):
        nums = int(input('Please pick 6 numbers from 1 - 99: '))
        t_list.append(nums)
    print(f'You chose: {t_list}')

    if pick_6() == t_list:
        balance += 25000000
    elif pick_6() == t_list[1]:
        balance += 100
    elif pick_6() == t_list[2]:
        balance += 100

    
    
    
pick_6()  
ticket()       











