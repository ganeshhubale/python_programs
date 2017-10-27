with open('my.txt', 'a') as fp:
    fp.write("hey you are  w here...")
    fp.close()
with open('my.txt') as fb:
    for m in fb:
        print(m)

