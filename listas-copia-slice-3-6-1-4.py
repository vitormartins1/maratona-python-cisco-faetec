# Se omitir o start no seu slice, assume-se que pretende 
# obter um slice começando pelo elemento com index 0.

#m y_list[:end]

# é um equivalente mais compacto de:
#m y_list[0:end]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# Da mesma forma, se omitir o end no seu slice, presume-se 
# que deseja que o slice termine no elemento com o index len(my_list).

# my_list[start:]

# é um equivalente mais compacto de:

# my_list[start:len(my_list)]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)