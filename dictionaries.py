states = {"Ghana": 10, "Nigeria": 36, "America": 52}
print(states)

#access values in the dictionary
print(f'Ghana has {states["Ghana"]} region')

#update dictionary values
states['Ghana'] = 8
print(states)

#Remove a key and its values from a dictionary

del (states["America"])
print(states)