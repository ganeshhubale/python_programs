n = int(input("Enter number of students: "))
info = {} # here

subjects = ('math','physics','chemistry','biology','english')

for i in range(0, n):
    name = input('Enter name of student %d: ' % (i + 1))
    marks = []
    for x in subjects:
        marks.append(int(input("Enter marks of %s:" % x)))
        
    info[name] = marks

for x, y in info.items():
    print(y[0],y[1],y[2],y[3],y[4])
    if y[1] > 35:
        total = sum(y)
        if total < 200:
            print("%s failed!" % x)
        else:
            print("%s pass! " % x)
    else:
        print("%s failed!" % x)

