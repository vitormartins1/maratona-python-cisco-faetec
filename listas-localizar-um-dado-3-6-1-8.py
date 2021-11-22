my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")


#---------------------------------------------
# Vamos supor que escolheu os seguintes números na 
# loteria: 3, 7, 11, 42, 34, 49.
# Os números que foram sorteados são: 5, 11, 9, 42, 3, 49.
# A questão é: em quantos números é que acertou?

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

