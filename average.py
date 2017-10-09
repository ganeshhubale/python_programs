n = int(input("Enter number of subjects:"))
sum = 0
a = 0
while a < n:
    m = int(input("Enter Marks:"))
    if m > 100:
        print("Invalid Data")
    else:
        sum = sum + m
        a = a + 1
sum = sum / n
print("Average of Marks= " + str(sum))
