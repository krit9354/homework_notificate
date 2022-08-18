number = 1
while number != 0:
    number = int(input())
    while number != 0:
        ten = number // 10
        number = number % 10
        one = number % 5
        five = number // 5
        print("ten:", ten)
        print("five:", five)
        print("one:", one)
        number = int(input())
