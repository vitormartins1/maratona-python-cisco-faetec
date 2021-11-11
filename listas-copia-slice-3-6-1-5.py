# omitindo ambos start e end faz uma cópia de toda a lista:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

# A instrução del é capaz de apagar mais do que apenas 
# um elemento de uma lista ao mesmo tempo - também pode apagar slices:

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# A eliminação de todos os elementos de uma só vez também é possível:

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

