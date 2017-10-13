def add():
        print ("Enter the two numbers to Add")
        fact = 1
        A=int(input("Enter A: "))
        if A==0:
        	return fact
        while(A>0):
        	fact= fact*A
        	A= A-1
        return fact


fact1=add()
print("Factorial = ", fact1)

