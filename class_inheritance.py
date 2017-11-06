class college:

    def __init__(self, name, col):
        self.name = name
        self.col = col
    def detail(self):
        print ("{} from {}".format(self.name, self.col))
class Teacher(college):
    def __init__(self, name, col, dept, subj):
        college.__init__(self, name, col)
        self.dept = dept
        self.subj = subj
    def details(self):
        print("{} from {} department with subject {} from {} college.".format(self.name, self.dept, self.subj, self.col))

c = college("Ram", "IIT")
c.detail()
t = Teacher("Ganesh", "RIT", "IT", "Math's")
t.details()


