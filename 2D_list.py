#⌨️ (2:29:37) 2D Lists

# My 2D list
my_list = [
 [1, 2, 3,10, 11],
 [4, 5, 6,12, 13],
 [7, 8, 9,14, 15]         
]
for list in my_list:
    print(list[0])


for list in my_list:
    for row in list:
        print(row)

print(my_list[0][3])
print(my_list[1][3])


# New 2D list
go_list = [
 ['fruit','snoep'],
 ['smal','big'],
 ['apple','orange']         
]
print(go_list)
print(go_list[0][0])
print(go_list[1][1])