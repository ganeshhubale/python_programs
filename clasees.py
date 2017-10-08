class Hello():
    def __init__(self):
        print("cllass objrect")

    def addition(self, a, b):
        return a+b

if __name__ == '__main__':
    h = Hello()
    print(h.addition(10,20))
