
n=int(input("Enter Number: "))
a, b = 0, 1
print(a, b)

while a < n:
    b = b + a
    print(b)
    a, b = b, a
