

class Math():
    def __init__(self, a, b):
        print("cllass objrect")

        self.a = a
        self.b = b

    def __add__(self, obj):
        return self.a + obj.b, obj.a + self.b

    def __sub__(self, obj):
        return self.a - obj.b, obj.a - self.b

    def __mul__(self, obj):
        return self.a * obj.b, obj.a * self.b


if __name__ == '__main__':
    m1 = Math(10, 20)
    m2 = Math(20, 30)
    
    print(m1 + m2)
    print(m1 - m2)
    print(m1 * m2)

                                                                               
                       
