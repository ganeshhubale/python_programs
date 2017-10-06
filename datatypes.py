datatypes--1]immutable 

a]string-->
--->	String1='hello i am ganesh'
	or
	String2="hello i am ganesh"
	
--->    for multiline

	''''''hello i am ganesh
	i am from rit
	its too good''''''
a1]concatenation->+
a2]repitition->*==>string1*2==>hello i am ganeshhello i am ganesh
a3]slicing->string1[2:7]==>llo i am ganesh
a4]indexing->string1[-1]+string2[1]==>he
examples=>string1[-1], string1[3], string1[:1], string1[3:6], string1[2:-3]

Type specific methods:
find()
replace()
split()
count()
upper()
max()
min()
isalpha()

b]numbers->
int-
float-
complex(3+2j) 



c]tupes 
-it is set of different data types
example--> tuple1={'ganesh',8.99,8}

2]mutable 

  a] lists-->
  list1=['ganesh',8.99,8]
append()
extend()
insert()
pop()
  
b]dictionaries

dict={1:'ganesh',2:'jtdhf',3:'onjhj'} 

dict.values()
dict[1]
len(dict)
dict.key()
items()
get()
update()
pop()
values()

c]sets

-unordered collection of items
-only includes unique elements

set1={1,2,3,4,5,9,3}

print set1 ==>1,2,3,4,5,9\

union -- set1 | set2
intersection -- set1 & set2
difference -- set1 - set2

================================
=======================
FLOW CONTROL

--------------
if ():


if ():
else:


if ():
..
elif ():
..
else:



for quant in range(start_point, end_point, icrement_value ):


while ():
..


break

continue---
for x in range(20):
	if(x%2)==0:
		continue
	print(x)

output:-- 1 3 5 7 ...

to take input from user
num=int(input('enter number'))

========================
functions in python
=============

1]built in functions
2]userdefined --
def fun_nm (a, b):
...
...
calling function==> fun_nm(x, y)

===========================
file handling in python
----------

x=open(filename, mode)
x.read()
x.write("hjghjcvkj")
x.seek(0)
 x.close()





