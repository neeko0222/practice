
# end = 'years old! Check out their popular albums: '

#how to merge two dictionaries? but is that ideal?



Rapper = {
    'name': ['kanye', 'lil uzi vert']
}

Age = {
    'kanye': 44,
    'lil uzi vert': 23
}

Album = {
    'lil uzi vert': ['luv is Rapper 2', 'eternal atake'], 
    'kanye': ['College Drop', 'Life of Pablo', 'Yeezus', 'Late Registration'],
}


# dirct.values 
def RapperCheck():
    
    # while true means loop forever!
         # made user inut translate to lowercase for case sens purposes
        user = str(input("Enter a Rapper ").lower())
    
        if user in Rapper.get('name'):

                # if user in Age.get(user):
                    print(user)
                    
                    

                


            # i want it to only return the matching user input
       

                # print (Rapper['name'])

        else:
            print('sorry ' + "'" + user + "'" + ' is not in our Rapperbase! ')


#what can i add into these parameters?
RapperCheck()




