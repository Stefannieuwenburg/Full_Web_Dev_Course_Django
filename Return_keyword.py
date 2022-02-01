#⌨️ (1:35:06) The Return Keyword


def add_num(num1,num2):
    return num1 + num2

num1=int(input('Enter first number :'))#singel nr 9
num2=float(input('Enter second number :'))#nr whit 0.0
print(add_num(num1,num2))


def add_numbers(num1,num2):
    return num1 + num2
print(add_numbers(4,4))


def my_function():
    return 5+4
print(my_function())


def greet (name):
    greeting = (f'Hello, {name}!')
    return greeting
print(greet('bob'))