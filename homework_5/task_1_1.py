class Person(object):
    def __init__(self,full_name,year):
        k=0;
        for s in full_name:
            if s==' ':
                k=k+1
        assert k==1
        assert year > 1900 and year<2019
        self.full_name = full_name

        self.BirthYear = year

    def Name(self):
        k=0
        for s in self.full_name:
            if (s != ' '):
                k=k+1;
            else:
                return self.full_name[:k]


    def Surname(self):
        k = 0
        for s in self.full_name:
            if (s != ' '):
                k = k + 1;
            else:
                return self.full_name[k+1:]

    def old_age(self,year=2019):
        return year-self.BirthYear

class Employee(Person):
    def __init__(self,full_name,year,position,salary,expirience):
        assert salary>=0
        assert expirience>=0
        Person.__init__(self,full_name,year)
        self.Position = position
        self.Salary = salary
        self.Expirience = expirience
    def Prefix(self):
        if (self.Expirience)<3:
            return "Junior "+self.Position
        else:
            if (self.Expirience>6):
                return "Senior " + self.Position
            else:
                return "Middle " + self.Position


    def BonusPlus(self,up):
        self.Salary = self.Salary + up;

class ITEmployee(Employee):
    def __init__(self,*args,**kwargs):
        Employee.__init__(self,*args,**kwargs)
        self.skills = [];
    def AddSkill(self,skill):
        self.skills.append(skill)
    def AddSkills(self, skills):
        for skill in skills:
            self.skills.append(skill)

p1 = Person("Petro Petrov",1929)
print(p1.Surname())
print(p1.Name())
print(p1.old_age())
print(p1.old_age(2021))

p2 = Employee("Petro Petrov",1939,"QA",1000,4)
print(p2.Surname())
print(p2.Name())
print(p2.old_age())
print(p2.old_age(2021))
print(p2.Prefix())
p2.BonusPlus(100)
print(p2.Salary)