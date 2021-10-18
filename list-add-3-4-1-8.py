numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#

numbers.insert(1, 333)
print(len(numbers))
print(numbers)

#

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

#

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

#

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

#

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

#