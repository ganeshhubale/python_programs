n = int( input("Enter number of students: "))
print ("Enter marks of three subjects")
a = 1
while n >= 1:
    print("Student Number : ",a)
    physics = int(input("marks of physics: "))
    history = int(input("marks of history: "))
    maths = int (input("marks of math's: "))
    total = physics + history + maths

    if total < 120:
        print("Failed")
    else:
        print("Pass")
    n -= 1
    a +=1

