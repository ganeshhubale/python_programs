
n=int(input("Enter Number: "))
a, b = 0, 1
print(a)
l = [0]
# l1 = [0]
while a < n:
    b = b + a
    print(b)
    x = b**3
    l.append(x)
    a, b = b, a
print(l)
