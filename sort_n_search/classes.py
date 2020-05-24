class Man:
    def __init__(self, age, sex, height, weight):
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight

    def print_me(self):
        print(self.age, self.sex)

    def index(self):
        index = self.weight/2.205/pow(self.height/39.37, 2)
        return index


man = Man(32, "Male", 180, 80)
print(man.index())
