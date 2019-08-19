#program that ask of your name and age and displays it to the screen with a welcome message
#The input() function waits for the user to type some text on the keyboard and press ENTER.
#name = input('what is your name :')
#age = input ('how old are you? :')
#print (f'Welcome {name} you are {age} years old')

age = input('How old are you? :')
money = input ('How much loan do you want? :')
name = input ('What is your name? :')

if (age < str(18) and money > str(2000)):
    print (f"{name} You are younger than 18 and can't qualify for a loan above 2,000 GHC")
else:
    print (f"Congratulations {name} you qualify for the loan of {money}")

