
def rot():
   abc = 'abcdefghijklmnopqrstuvwxyz'

   phrase = input('Enter a phrase: ')
   shift = int(input('How many times do you want to shift?: '))

   x = len(phrase)

   cipher = ''

   for i in range(x):
      char = phrase[i] #breaks down phrase
      loc = abc.find(char) #finds location of phrase in abc
      new_loc = (loc + shift) % 26 #creates var to move whatever is put in shift...
      #print(char, loc, new_loc)
      cipher = cipher + abc[new_loc] 

   print(cipher)

rot()