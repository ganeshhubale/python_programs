list1 = [1, 2, 3]
def squareof(num):
    return num * num
print(list(map(squareof, (1, 2, 3))))
"or we can use list"
print(list(map(squareof, list1)))

