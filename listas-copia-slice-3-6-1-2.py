# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#A new_list lista terá end - start (3 - 1 = 2) elementos - 
# aqueles com índices iguais a 1 e 2 (mas não 3).