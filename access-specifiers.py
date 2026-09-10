class Student:

    def __init__(self):
        self.name = "Alex"          # Public
        self._age = 20              # Protected
        self.__password = 1234      # Private


student = Student()

# 1. PUBLIC
# Can be accessed directly from outside the class.
print(student.name)


# 2. PROTECTED
# Can technically be accessed, but _ indicates:
# "This is intended for internal/subclass use."
print(student._age)


# 3. PRIVATE
# Direct access gives an AttributeError because
# Python has name-mangled __password.
# print(student.__password)       # ERROR

# Python internally changes:
# __password  →  _Student__password
#
# So it can technically still be accessed like this:
print(student._Student__password)
