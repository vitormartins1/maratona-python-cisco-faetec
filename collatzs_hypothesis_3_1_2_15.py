c0 = int(input("Enter a number: "))
steps = 0

if c0 < 1:
    print("Use a non negative, non zero number.")
else:
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        print(c0)
        steps += 1

    print("Total steps: ", steps)

