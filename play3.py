
Goat = {
    
    'name': 'kanye',
    'age': 44,
    'albums': ['College Drop', 'Life of Pablo']

 
}

user = str(input())

# print (Goat.get('age'))
# print(Goat['age'])



def ageCheck():
    if user in Goat.values():

        print(Goat['age'])
    else:
        print('sorry ' + user + ' is not in our database! ')

ageCheck()




# print (rappers['Kanye'])

# def oldhead():

#      if user in rappers:


    # return rappers['Kanye']
    # if user in rappers:
    #     print('gj')
    # else:
    #     print('sorry hun')
