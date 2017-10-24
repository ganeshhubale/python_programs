a = [1, 2, 3]
print("List=",a)
# insert_element_in_list-a
a.insert(0,4)
print("Insertion of 4 at 0th postio =",a)

# append

a.append("ganesh")
print("append =",a)

# count

print("count of ganesh = ",a.count('ganesh'))

# remove
a.remove('ganesh')
print("remove ganesh = ",a)

# reverse
a.reverse()
print("reverse = ",a)

# length

print("Length = ",len(a))

# extend
b = [1, 2, 3]
a.extend(b)
print("List b is added to list a = ",a)

# sort
a.sort()
print("sorting = ",a)
# delete
del a[1]
print("a[1] is deleted = ",a)
# for x in a:
x = 1
for x in a:
    print(x)
