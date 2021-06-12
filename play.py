# class Dog:
#     attr1 = "mammal"
#     attr2 = "dog"
    
#     def fun (self):
#         print("I'm a", self.attr1)
#         print("he is a", self.attr2)


# Rodger = Dog()        

# print(Rodger.attr1)
# Rodger.fun()


import random

list_one = ["Kanye", "Drake", "Kodak"]
list_two = ["Lil Uzi Vert", "Lil Peep", "Jay Z"]
list_three = [1,2,3]
list_four = [4,5,6]

combined = list_one, list_two
numbers = list_three, list_four


numbers = random.choice(random.choices(numbers, weights=map (len, numbers))[0])

rapper = random.choice(random.choices(combined, weights=map (len, combined))[0])
print(numbers)

    





        

# p = Fight('Neeko', 'Keke')
# p.who_won()


