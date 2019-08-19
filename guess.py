import random 

guess, random_guess = random.randint(0, 10), 0
while guess != random_guess:
    random_guess = int(input("Enter a guess : "))
    print(f"Random number between 0 and 10 is {guess}")
print ("Congrats, you guessed correctly")