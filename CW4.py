class Person:
    firstName: str
    secondName: str

    def __init__(self, firstName: str, secondName: str):
        self.firstName = firstName
        self.secondName = secondName

    def info_person(self):
        print(f'{self.firstName} | {self.secondName}')