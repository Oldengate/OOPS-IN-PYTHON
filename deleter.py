class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        del self._age
        
p = Person(20)

print(p.age)     # getter
p.age = 25       # setter
del p.age        # deleter
