class Employee():
    '''Collect info about an employee.'''

    def __init__(self, first, last, salary=50000):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self):
        self.salary + 5000
