
def rot():
   abc = 'abcdefghijklmnopqrstuvwxyz'

   phrase = input('Enter a phrase: ')
   shift = int(input('How many times do you want to shift?: '))

   x = len(phrase)

   cipher = ''

   for i in range(x):
      char = phrase[i] 
      loc = abc.find(char) 
      new_loc = (loc + shift) % 26 
      cipher = cipher + abc[new_loc] 

   print(cipher)

rot()