l1=[]
l2=[]
sum2=0
sum1=0
for i in range(20):
    if i % 2 == 0:
        l1.append(i)
        sum2+=i      
    else:
        l2.append(i)
        sum1+=i
else:
    print (l1)
    print (sum2)
    print (l2)
    print (sum1)
