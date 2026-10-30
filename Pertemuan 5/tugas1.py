class Person:
    def __init__(self, name='', date_of_birth='', parents='', children=''):
        self.name = name
        self.date_of_birth = date_of_birth
        self.parents = parents
        self.children = children

class Student(Person):
    def __init__(self, name='', date_of_birth='', parents='', children='', student_id=''): 
        super().__init__(name, date_of_birth, parents, children)
        self.student_id = student_id

class Employee(Person):
    def __init__(self, name='', date_of_birth='', parents='', children='', employee_id=''): 
        super().__init__(name, date_of_birth, parents, children)
        self.employee_id = employee_id