"""
try:
    if b > 7:
        print('Yes')
except:
        print('Check for errors')
"""


while True:
    try:
        phone = int(input("Enter your phone number: "))
        break
    except ValueError:
        print("That is not a valid number, please try again..")