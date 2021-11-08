# perde o valor armazenado previamente

variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2

#----------------

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

#----------------

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1