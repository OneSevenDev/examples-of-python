class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_person(self):
        return '<Person ({0}, {1})'.format(self.name, self.age)

p = Person('Manuel', 21)
print('Type of Object: {0}, Memory Address: {1}'.format(type(p), id(p)))