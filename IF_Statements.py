# ⌨️ (1:40:45) IF Statements In Python

a = 4
b = 3

if a > b:
    print(f'nr {a} is greater than {b}' )  # Also posibol to show the nr in site the text print
elif a != b:
    print(f'nr {a} is same as nr {b}' )
elif a < b:
    print(f'nr {a} is smaller than nr {b}' )  
elif a == b:
        print(f'nr {a} is same as nr {b}' )
else:
    print(f'none of them')
    

x = 35
y = 33
c = False

if x > y:
  print(f'x is groter dan y')
elif x == y:
  print (f'x is gelijk aan y ')
elif c == False:
  print(f'c is False')
elif c == True:
      print(f'c is True')
else: 
    print(f'no al of that')
    
boy = True
short = True

if boy == True or short == True:
    print(f'he is a boy and he is short')
elif boy == False:
    print(f'he is not a boy')
else:
    print(f'not of them')
    













languages = 'javascript'

def train_if_else():
    if languages == 'java':
        print('Conditianal is java')
    elif languages == 'python':
        print('Conditianal is python')
    elif languages == 'javascript':
        print('Conditianal is javascript')    
    else:
        print('diffrent languages')
        
#train_if_else()