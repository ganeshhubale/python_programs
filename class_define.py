class person:

    def __init__(self,name):

        self.name = name
    def details(self, branch, mark):
        self.branch  = branch
        self.mark  = mark
        print("{} is student of the {}. He got {} percent marks.".format(self.name, self.branch, self.mark))

p = person("ganesh")
p.details("IT", 99)

