# -a adding task
# -d deleting the task
# -v viewing the task
# python3 todoapp.py -a 'creating the game'
#try:
#    3/0

#except Exception as e:
#    print(e)

#finally:
#    print("not working")


import sys
import os


s=sys.argv[1:]

if s[0] == '-a':
    with open('todo.text', 'w') as f:
        f.write("\n"+" ".join(s[1:]))

if s[0] == '-v':
    contents = None
    with open('todo.text', 'r') as f:
        contents = f.read()
    print(contents)

if s[0] == '-d':
    contents = None
    open('todo.text', 'r') as f:
        contents = f.read()
    print(contents)



