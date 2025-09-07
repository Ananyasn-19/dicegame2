# user input to roll dice:yes/no
# if the usersay yes(y) generate two random numbers
# print thrm
# if user input is no print "thank you for playing"
# if user entered anything apart 'y' or 'n' print "invalid input"



import random

while True:
    choice=input("Roll the dice (y/n): ").lower()
    if choice == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'({dice1},{dice2})')
    elif choice == 'n':
        print("Thank you for plaing")
    else:
        print("invalid choice")
