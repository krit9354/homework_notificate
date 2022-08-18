i = 1
j = 1
total = 0
while i <= 10000:
    while  j < i:
        if i % j == 0:
            total += j
        j+=1
    if total == i:
        print(total)
    total = 0
    i += 1
    j = 1
