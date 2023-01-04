i = 1
while i < 6:
    print(i)
    i += 1


# break statement is used to interrupt a loop
b = 1
while b < 6:
    print(b)
    if b == 3:
        break
    b += 1


#continue statement is used to stop the current iteration
c = 0
while c < 6:
    c += 1
    if c == 3:
        continue
    print(c)

#else statement runs code when one condt is no longer true
k = 1
while k < 6:
    print(k)
    k += 1
else:
    print('k is no longer less than 6')
