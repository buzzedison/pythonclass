#list in python
countries = ['Ghana', 'Senegal', 'Nigeria', 'England']
#print (countries[0]) #ghana
#print (countries[3])#england
#print (countries[0:2])
#print(countries[:-1])
countries.append('Jamaica') #add jamaica to the list 
print(countries)
#change the value of an item on the list. e.g Nigeria to India
countries[2] = 'India'
print(countries)
#delete an item from the list
del countries[1] #this will delete Senegal from the list. It is in the index of 1
countries.remove('Ghana')         ## search and remove that element
print(countries)

#check for the number of items on your list
print(len(countries))

# You can add lists together. 
#e.g let us create a new list and add the values of our first list and the newly created list.
states = ['Accra', 'New Delhi', 'Lagos', 'London' ]
print(countries + states)
#multiply a list
print(states * 2)

print(max(states))
print(min(states))