
print("Welcome to my python")


yam = 6545
rice = 88888888
food = yam * rice
print (food)

#print ('Welcome to my course')

firstName = 'Thomas'
lastName = 'Ade'
print(f'my name is {firstName} and my surname is {lastName}')
print(len(lastName))  #length of 

#print(abs(4/3)) 

"""
returns the absolute value of a numeric value (e.g. integer or float). 
Obviously it can’t be a string.
 It has to be a numeric value.
 """
 #print(round(-4/3))
 #returns the rounded value of a numeric value.
"""
#edison, dela, ewura = 18, 14, 12
#print(dela)

edison = dela = ewura = 15
print(edison)

name, age, school = 'Abigail', '20', 'Codewit Code School'
print(name, age, school)


#arithmetic operators

oranges = 40
pineapples = 17
mangoes = 5

print (oranges + pineapples)  #addition 
print (pineapples - mangoes)  #subtraction 
print (oranges * mangoes)  #multiplication
print (pineapples / mangoes) #division
print (pineapples % mangoes)  #modular

#Strings
homePage = 'Welcome to my application'  #string
print(homePage)
#assign String values to variables and print them in a statement
firstName = 'Edison'
lastName = 'Ade'
print(f'my name is {firstName} and my surname is {lastName}')

print ('x' * 20) #we can multiply strings by integer

news = 'You just won the $1 million dollar lottery'
#pint the index for just
print(news[0])  #in programming, including python we start counting from 0
print(news[3:8]) #indexing more than one character. 
print (news[:9])
print (news[:-4]) #print all except the last four characters.

#placeholder 
myName = "Eddy"
money = "%s has a million us dollars"

print(money%myName)
result:
Eddy has a million us dollars
print (money%('Abigail'))
result:
Abigail has a million us dollars

#More String formatting
#name = input ('what is your name:')
#print (f'Hello {name}')
#print ('Hello', name)

#Replacing Multiple Values (placeholder)
quiz = "%s %s are the winners of the national science and maths quiz"
print(quiz% ("Wesley Girls", " and Holy Child"))

statement = "%s has %d number of states"
print (statement%('America', 52))

#using .format for string placeholder.

print ('How to say Good morning in French is {}'.format('Bonjour!'))

#we can also do this
language = '{} is the official language of {}'
print (language.format('English', 'Ghana'))
"""
#Reordering Formatters with Positional and Keyword Arguments
#print ('top {0} states in {1} are {2}, {3}, {4}'.format(3, 'France', 'Paris', 'Boardeaux', 'Nantes'))

#print(min(7,5, 8, 3))
#print(max(11, 2, 6, 22, 43))
num = [11, 22, 7, 9, 16, 99]
print(sum(num))