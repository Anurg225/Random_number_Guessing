import random
number_guess=random.randint(1,100)
guess =None
tries=0
print("Welcome to Number guessing")
while guess!=number_guess:
    try:
        guess=int(input("Enter the number between 1 and 100:"))
        tries=tries+1
        if(guess<number_guess):
            print("Number is  to small")
        elif( guess>number_guess):
            print("Number is too large")
        else:
            print(f"Congrats you find a number in {tries} try")
    except ValueError:
        print("you enter a invalid number")   
