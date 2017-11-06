class student:

    def __init__(self, name, mark, rollno):
        self.name = name
        self.mark = mark
        self.rollno = rollno
    def info(self):
        print("Name: {}\nMarks: {}\nRoll No.: {}".format(self.name, self.mark, self.rollno))
std1 = student('ganesh',95, 1404018)
std1.info()


