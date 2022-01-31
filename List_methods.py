# list methods
list0 = [1,2,3,4,5,6,7,8]
list1 = [4,3,5,9,6,8,7]
list2 = ['banana','apples','mango','orange']

#delete insite a list
del list1[0]
print(list1)

#pop things from a list also by index nr
list2.pop(1)
print(list2)
# copy a list
list3 = list2.copy()
print(list3)

# list up site down
list2.reverse()
print(list2)

# sort method on right ordering
list1.sort()
print(list1)

# extra add to the list
list2.append('cherry')

# extend is connect the 2 listen to gether
list1.extend(list2)

# to get the length of the list
print(len(list2))

# insert a thing to the list on place
list2.insert(0, 'cherry')

#remove the thing from the list
list2.remove('banana')

#clear a list
#list2.clear()

# to get the index nr of mango
print(list2.index('mango'))

# to get the count of a list item
print(list2.count('mango'))
