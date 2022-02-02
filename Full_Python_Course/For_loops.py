#⌨️ (2:19:47) For Loops In Python
from rich import print


mydict = {
    'name': 'Tim',
    'age': 36, 
}
for values in mydict:
    print (values)


my_list = ['ji','hi','lo','po']
for values in my_list:
    print(values)
    if values == 'lo':
        break


for letter in 'hello':
    print(letter)
else:
    print('finished with loop')


#for loop met function
names = ['Bob', 'Shaun', 'Preeti', 'Jeff']
def lijst_names():
    for x in names:
        print(f'Hello, {x}!')
lijst_names()


# for loop in for loop
explain = ['rood','groot','lekker']
fruit = ['appel','orange','kers']
for x in explain:
  for y in fruit:
    print(x, y)