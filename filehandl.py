def write_file(text):
    with open('sample.text', 'w') as f:
        f.write(text)

def read_file():
    contents = None
    with open('sample.text', 'r') as f:
        contents = f.read()
    return contents

raw_text = """
hello RIT Islampur, MH, India

i am ganeesh
but people are sleeping
zzzzzzzzzzz
"""

write_file(raw_text)
print(read_file())
