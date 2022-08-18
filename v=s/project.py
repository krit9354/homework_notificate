def teacher_pun_beautiful():
    while True:
        mode = input("run or stop(y/n):")
        if mode == "n":
            break
        if mode == "y":
            s = input("ระยะทาง(เมตร):")
            t = input("เวลา(วินาที):")
            v = float(s) / float(t)
            print("ความเร็ว =",v,"เมตร/วินาที")

teacher_pun_beautiful()