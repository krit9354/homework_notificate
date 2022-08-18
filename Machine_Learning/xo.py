def show():
    for i in range(3):
        print()
        for j in range(3):
            print(data[block[i][j]],end ="|")
    print()

def mark_block(choose,player):
    i,j = position[choose]
    block[i][j] = player

def check_win():
    #แนวนอน
    for i in block:
        if sum(i) == 3:
            print("x win")
            return False
        elif sum(i) == -3:
            print("o win")
            return False
    #print("นอน")
    #แนวตั้ง
    for i in range(3):
        if block[0][i]+block[1][i]+block[2][i] == 3:
            print("x win")
            return False
        elif block[0][i]+block[1][i]+block[2][i] == -3:
            print("o win")
            return False
    #แนวทะแยงซ้ายไปขวา
    #print("นอนตั้ง")
    s = 0
    for i in range(3):
        s += block[i][i]
    if s == 3:
        print("x win")
        return False
    elif s == -3:
        print("o win")
        return False
    #print("แนวทะแยงซ้ายไปขวา")
    #แนวทะแยงขวาไปซ้าย
    if block[0][2]+block[1][1]+block[2][0] == 3:
        print("x win")
        return False
    elif block[0][2]+block[1][1]+block[2][0] == -3:
        print("o win")
        return False
   # print("แนวทะแยงขวาไปซ้าย")
    return True

    



position = {
    1:[2,0],
    2:[2,1],
    3:[2,2],
    4:[1,0],
    5:[1,1],
    6:[1,2],
    7:[0,0],
    8:[0,1],
    9:[0,2]
}
block = [[0,0,0],
         [0,0,0],
         [0,0,0]]
data = {0:"-",1:"x",-1:"O"}
status = 1
run = True

while run:
    play = int(input(f"player {data[status]} :"))
    mark_block(play,status)
    if status == 1:
        status = -1
    else:
        status = 1
    show()
    run = check_win()

    
