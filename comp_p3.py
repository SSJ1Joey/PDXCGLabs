#Write a dictionary comprehension to swap keys and values of a given dictionary...

simple_dict = {'a': 1, 'b': 2}

print({v:k for k,v in simple_dict.items()})



#for keys, values in simple_dict.items:
    #print(v, k)