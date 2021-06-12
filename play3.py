
end = 'years old! Check out their popular albums: '

# what does this do?
# from collections import defaultdict
#how to merge two dictionaries! but is that ideal?



Age = {
    'name': ['kanye', 'lil uzi vert'],
     'age': [44,22]
}


Album = {
    'lil uzi vert': ['luv is rage 2', 'eternal atake'], 
    'kanye': ['College Drop', 'Life of Pablo', 'Yeezus', 'Late Registration'],
}


# made user inut translate to lowercase for case sens purposes
user = str(input("Enter a Rapper ").lower())




# .values is what I was looking for
def ageCheck():
    # what can i put in the values parameter
    # is there a way to only have print

  
    if user in Age.get('name'):
        print(Age['age'])
    else:
        print('sorry ' + "'" + user + "'" + ' is not in our Agebase! ')


#what can i add into these parameters?
ageCheck()




