#list comp       #functional programing

#list between 1 and 10

def squares():
    my_squares = []
    for number in range(1, 11):
        my_squares.append(number ** 2)
    return my_squares

#this = def_squares()
print([number ** 2 for number in range(1, 11)])


a_dict.values() #returns values only
        keys() #returns keys only
        items() #returns items only


import string
print({char: ord(char) for char in string.ascii_lowercase})

a_dict = {}
for char in string.ascii_lowercase:
    a_dict.update({char: ord(char)})