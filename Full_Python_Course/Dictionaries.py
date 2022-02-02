#⌨️ (2:05:05) Dictionaries In Python
from rich import print

my_dict = {
    'name': 'Tim',
    'nationality':'Hollander',
    'age':20, 
    'friends':['pieter','paul','magda'],
    'is_tall':True,
}
z = (my_dict['is_tall'])
print(z)
x = (my_dict['age'])  # End so one
print(x)
y = (my_dict['nationality'])
print(y)
# print full dict
print(my_dict)


# dictionary of Comprehensions
names = ['Bruce','Clark','peter','logan','Wade']
heros = ['Batman','Superman','spiderman','Wolverine','Deadpool']

# i whant !!! whit zip functie

hero_dict = {}
for name, heros in zip(names, heros):
    hero_dict[name] = heros

print(hero_dict)

#dict list Comprehension
hero_dict = {
    name: hero for name,
    hero in zip (names, heros)
}
print(hero_dict)

