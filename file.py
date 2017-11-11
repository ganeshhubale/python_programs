with open('my.txt', 'w') as fo:
    fo.write("hello")
    fo.close()
with open('my.txt', 'a') as fl:
    fl.write("next")
    fl.close()

with open('my.txt', 'r') as fp:
    print(fp.read())
    fp.close()

    
