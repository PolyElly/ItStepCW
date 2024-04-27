class SubjectMKA:
    name: str
    hours: int
    estimation: float
    enable: bool

    def __init__(self, name: str, hours: int, estimation: float, enable=True):
        self.name = name
        self.hours = hours
        self.estimation = estimation
        self.enable = enable

    def info_subject(self):
        if self.enable:
            print(f'{self.name} | {self.hours} | {self.estimation}')
        else:
            print(f'{self.name} is not studying')

python = SubjectMKA(name='PySenior', hours=18, estimation=10.8)
# python.show_info()

class Student:
    firstName: str
    secondName: str
    subject: SubjectMKA


    def __init__(self, firstName: str, secondName: str, subject: SubjectMKA):
        self.firstName = firstName
        self.secondName = secondName
        self.subject = subject

    def info_peson(self):
        print(f'{self.firstName} | {self.secondName}')
        self.subject.info_subject()

cake = Student(firstName='Polyanna', secondName='Cake', subject=python)
cake.info_peson()

class StudyGroup:
    name: str
    students: int
    learningdays: str

    def __init__(self, name: str, students: int, learningdays: str):
        self.name = name
        self.students = students
        self.learningdays = learningdays

    def infoGroup(self):
        print