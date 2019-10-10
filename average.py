
num_list = []

def average():
    while True:
        x = int(input('Please enter your numbers or type done: '))
        num_list.append(x)
        if x == 'done':
            num_list.remove('done')
            main() 
            break
            
           

def main():
    print(num_list)
    print(sum(num_list)/len(num_list))
    

average()
main()




            
            









        
            


