#⌨️ (3:25:17) Building A Simple Login and SignUp System

#//////Login and SignUp System\\\\\\\\\
    
print('Creat account to login')

username = input("Enter username: ")
password = input("Enter password: ")

print('your account has been created successfully')
print('Login now!')

username2 = input("Enter username: ")
password2 = input("Enter password: ")

if username == username2 and password == password2:
    print('Login successfully')
else:
    print('Invalid credentials')