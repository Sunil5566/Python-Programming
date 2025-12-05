class Student:
    def __init__(self, phy, chem, bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio

    @property
    def percentage(self):
        return str((self.phy + self.bio + self.chem) / 3) + "%"

stu1 = Student(98,98,98)
print(stu1.percentage)

stu1.phy = 79
print(stu1.percentage)
