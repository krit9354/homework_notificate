number = 1
i = 1#ตัวประกอบ
sum_i = 0
a = []
while number <= 100000:
    print("number:",number)
    while i < number:
        if number % i == 0:
            sum_i = sum_i + i
        i = i + 1
    if sum_i == number:
        a.append(number)

    number = number + 1

    i = 1
    sum_i = 0
print(a)