#⌨️ (1:22:33) Functions In Python


name1 = input('enter your name :')
age1 = input('input your age :')

def greet(name1, age1):# moet argumenten geven  i.v.m input veld in de functie
    print(f'your name is {(name1)} and your age is {(age1)}')


def greetings(*name):
    print(f'Welkom {(name)[0:3]}')
     
#greetings(f'Tim','john','tommy')

def greetings_functions(name, age):
    print(f'welkom {(name)} you are {(age)} old')
     
#greetings_functions('hi', 18)
greet(name1,age1)