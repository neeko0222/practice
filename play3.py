end = 'years old'


Goat = {
    
    'name': 'kanye',
    'age': 44,
    'albums': ['College Drop', 'Life of Pablo']

 
}

user = str(input("Enter a rapper ").lower())




# to check if a value is in a dictionary if x in d.values()
def ageCheck():
    # what can i put in the values parameter?

    if user in Goat.values():
        print(' is about ')
        print(Goat['age'])
        print(end)
    else:
        print('sorry ' + "'" + user + "'" + ' is not in our database! ')

ageCheck()




# print (rappers['Kanye'])

# def oldhead():

#      if user in rappers:


    # return rappers['Kanye']
    # if user in rappers:
    #     print('gj')
    # else:
    #     print('sorry hun')
