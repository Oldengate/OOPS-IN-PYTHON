class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative")


p = Person(20)

print(p.age)   # getter
p.age = 25     # setter
print(p.age)
