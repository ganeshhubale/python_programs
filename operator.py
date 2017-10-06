#Arithmetic operations
num1 = 10
num2 =3.0
print "addition of num1 and num2", num1+num2
print "multiplication of num1 and num2", num1*num2
print "substractio of num1 and num2", num1-num2
print "division of num1 and num2", num1/num2
print "num1 rase to num2", num1**num2
print "Float division of num1 and num2", num1//num2
print "addition of num1 and num2", num1%num2

#Assignment operations

num3=num1+num2
num3+=num2

print "num3=num1+num2 and num3+=num2 =", num3

#comparison operators

# < > == !=

print "num1 > num2 =", num1>num2

#logical operators---and or not

x=True
y=False

print "x and y==",x and y
print "x or y==",x or y
print "not y==", y

#Bitwise operator

# & and operation 7->111 & 5->101 = 101
# | or operation  7->111 & 5->101 = 111
# ^ xor operation 7->111 & 5->101 = 010
#<< >>

print "7 & 5 = ", 7 & 5
print "7 | 5 = ", 7 | 5
print "7 ^ 5 = ", 7 ^ 5

print "5 << 2 =", 5 << 2 
print "5 >> 2 =", 5 >> 2 

#identity opearator
# IS --REFERES TO SAME OBJECT(true if opearator is identical), IS NOT--REFERES TO SAME OBJECT(true if opearator is identical)
x=5
print "x=5 is-->", x is 5
print "x is not 5-->", x is not 5
#membership operator
#in -->checks value present in list or not
#not in-->checks value present in list or not

x=[1,2,3,4,5]

print "x=[1,2,3,4,5]==>3 in list-->", 3 in x;
print "x=[1,2,3,4,5]==>5 not in list-->", 5 not in x;

