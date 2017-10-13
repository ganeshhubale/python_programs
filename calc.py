def add():
        print ("Enter the two numbers to Add")
        A=int(input("Enter A: "))
        B=int(input("Enter B: "))
        print ("addition = ",A + B)

def sub():
        print ("Enter the two numbers to Subtract")
        A=int(input("Enter A: "))
        B=int(input("Enter B: "))
        print ("Substraction = ",A - B)        

def mul():
        print ("Enter the two numbers to Multiply")
        A=int(input("Enter A: "))
        B=int(input("Enter B: "))
        print ("Multiplication = ",A * B)

def div():
        print ("Enter the two number to Divide")
        A=float(input("Enter A: "))
        B=float(input("Enter B: "))
        print ("Division = ",A / B)

print ("1: ADDITION")
print ("2: SUBTRACTION")
print ("3: MULTIPLICATION")
print ("4: DIVITION")
print ("0: QUIT")

while True:

    CHOICE = int(input("ENTER THE CORRESPONDING NUMBER FOR CALCULATION ")) 

    if CHOICE == 1: 
        print ("ADDING TWO NUMBERS:")
        add()

    elif CHOICE == 2:
        print ("SUBTRACTING TWO NUMBERS")
        sub()

    elif CHOICE == 3:
        print ("MULTIPLYING TWO NUMBERS")
        mul()

    elif CHOICE == 4:
        print ("DIVIDEING TWO NUMBERS")
        div()

    elif CHOICE == 0:
        exit()
    else:
        print ("The value Enter value from 1-4")

