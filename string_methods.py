s = "hello I am from R.I.T 172.22.2.225\n"

print("methods on String: ",s)

print("split : ",s.split(" "))

w = s.title()
print("Title : "+w)

w = s.upper()
print("upper : ",w)

w = s.lower()
print("lower : ", w)

w = s.swapcase()
print("swapcase : ",w)

print("isalpha : ",s.isalpha())

print("isalphanumeric : ",s.isalnum())

print("isdigit : ",s.isdigit())

print("islower : ",s.islower())

print("isupper : ",s.isupper())

print("istitle : ",s.istitle())

print("strip : ",s.strip())

print("left strip : ",s.lstrip("hello"))

print("right strip : ",s.rstrip('172.22.2.225\n'))

print(s.startswith("hel"))

print(s.endswith("225"))

print(s.find("I"))

print("reverse string: ",s[::-1])

print("Number of words in string :%d "% len(s.split(" ")))

print("join : ","-".join(s))

