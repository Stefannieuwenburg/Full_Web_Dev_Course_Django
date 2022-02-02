#⌨️ (3:16:43) Inheritance In Python
from New_student import Student

class Person(Student):
    pass
p1 = Person()
print(p1.name)
    
if p1.name == 'Tim':
    print('Yes it is Tim')
else:
    print('No it is not Tim')