#⌨️ (3:09:17) Classes and Objects In Python

class MyClass:
    id = 5
person1 = MyClass()
print(person1.id)


name = input('Enter your name: ')
age = input('Enter your age: ')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
student = Person(name,age)
print(student.name)
print(student.age)