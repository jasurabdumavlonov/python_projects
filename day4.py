import random

name_string = input("Gimme everybody's names,seperated by a comma. ")
splitted = name_string.split(', ')

name = random.choice(splitted)
print(f"{name} is going to buy a meal today!")

# ran = random.randint(0,len(splitted)-1)
# name = splitted[ran]
# print(name)

