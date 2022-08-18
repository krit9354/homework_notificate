import random

a = [
    ["localing an object using sound waves and echoes","echolocation"],
    ["to notice, to observe, to find ","detect"],
    ["able to sense or feel in a stronger than normal way","sensitive"],
    ["to adjust","adapt"],
    ["strange ","peculiar"],
    ["to (cause to) move up or away atter hiting a surface","bounce"],
    ["to fill tightly or completely by pushing something into something else","stuff"],
    ["the area at the back of the eye that receive light and send pictures of what the eye sees to thebrain","retina"],
    ["very modern and with all the newest features","cutting-edge"],
    ["to bring back into use","restore"],
    ["causing a lot of damage or destruction","devastating"],
    ["a nerve ending that reacts to a change, such as heat or cold, in the body by sending a message to the central nervous system","receptor"],
    ["to pass something from one place to another","transmit"],
    ["difficult to use, do, or deal with","awkward"],
    ["simple and not skillfully done or made","crude"]
    ]

point = 0
start = 1   #ข้อที่เริ่ม
last = 15    #ข้อสุเท้าย
round  = []
while len(round) != (last-start+1):
    c = random.randint(start-1,last-1)
    if c not in round:
        round.append(c)

for i in round:
    print(a[i][0])
    b = input(">>>")
    if b == a[i][1]:
        print("correct")
        point += 1
    else:
        print("wrong the correct is :"+a[i][1])
print("your score :",point,"/",last-start+1)




