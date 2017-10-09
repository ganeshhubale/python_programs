
n = (int(input("Enter Number:")))
i = 1
flag = 0
x = n//2

if n == 2:
    print("2 is prime number")
else:
    while i < x:
        if n % i == 0:
            flag = flag + 1
        i = i+1

    if flag > 1:
        print(str(n)+" is not  prime number")
    else:
        print(str(n) + " is prime number")
        
