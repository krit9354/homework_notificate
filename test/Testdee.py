import random
num = random.randint(1, 100)
user = 1
while user != 0:
    user = int(input())
    if user < num and user > 0:
        print("น้อยไป")
    if user > num:
        print("มากไป")
    if user == num:
        print("win!!!")