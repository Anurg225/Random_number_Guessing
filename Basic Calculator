import math
def menu():
    print("What do you want to do")
    print("Only shown Operation is allowed")
    print("1.Basic Mode(+,-,*,/)")
    print("2.Scientific Mode(sin,cos,log,square root,factorial)")
    print("3.Programmer Mode(BINARY,OCTAL)")
def basic_mode():
    b=input("Enter the operation:")
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the Second Number:"))
    match(b):
        case '+':
            result=num1+num2
            print("Your result is ",result)
        case '-':
            result=num1-num2
            print("Your result is ",result)
        case '*':
            result=num1*num2
            print("Your result is ",result)
        case '/':
            result=num1/num2
            print("Your result is ",result)
        case '%':
            result=num1%num2
            print("Your result is ",result)
        case _:
            print("Enter valid Operation")
def scientific_mode():
    print("1.Sin(x)")
    print("2.cos(x)")
    print("3.log(x)")
    print("4.Square root(x)")
    print("5.Factorial(x)")
    c= int(input("Select the operation number"))
    match(c):
        case 1:
            val=float(input("Enter the value in degree"))
            radiant=math.radians(val)
            result=math.sin(radiant)
            print("Your result is",result)
        case 2:
            val=float(input("Enter the value in degree"))
            radiant=math.radians(val)
            result=math.cos(radiant)
            print("Your result is",result)
        case 3:
            val=int(input("Enter the value:"))
            result=math.log(val)
            print("Your result is",result)
        case 4:
            val=int(input("Enter the value:"))
            result=math.sqrt(val)
            print("Your result is",result)
        case 5:
            val=int(input("Enter the value:"))
            result=math.factorial(val)
            print("Your result is",result)
        case _:
            print("Enter valid number")
def programmer_mode():
    print("Programmer Mode:")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Binary to Decimal")
    print("4. Octal to Decimal")

    choice = input("Select an operation (1–5): ")

    match choice:
        case "1":
            try:
                num = int(input("Enter decimal number: "))
                print("Binary:", bin(num)[2:])
            except ValueError:
                print("Invalid input! Enter an integer.")

        case "2":
            try:
                num = int(input("Enter decimal number: "))
                print("Octal:", oct(num)[2:])
            except ValueError:
                print("Invalid input! Enter an integer.")

        case "3":
            try:
                binary = input("Enter binary number: ")
                print("Decimal:", int(binary, 2))
            except ValueError:
                print("Invalid binary number!")

        case "4":
            try:
                octal = input("Enter octal number: ")
                print("Decimal:", int(octal, 8))
            except ValueError:
                print("Invalid octal number!")

        case "5":
            print("Returning to Main Menu...")

        case _:
            print("Invalid choice.")



menu()
a=int(input("Enter Mode No."))
if (a==1):
   basic_mode()
elif(a==2):
   scientific_mode()
else:
    programmer_mode()
