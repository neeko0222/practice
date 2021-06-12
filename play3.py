
end = 'years old! Check out their popular albums: '

Goat = {
    'name': 'kanye',
    'age': 44,
    'albums': ['College Drop', 'Life of Pablo']
}






# made user inut translate to lowercase for case sens purposes
user = str(input("Enter a rapper ").lower())




# .values is what I was looking for
def ageCheck():
    # what can i put in the values parameter
    # is there a way to only have print
    if user in Goat.values():
        print('is about ')
        print(Goat['age'])
        print(end)
        print(Goat['albums'])

    else:
        print('sorry ' + "'" + user + "'" + ' is not in our database! ')


#what can i add into these parameters?
ageCheck()




