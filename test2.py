
score = int(input("score:"))
if (score >=0) and (score <=49):
    print("grade : F")
else:
    if score <=59:
        print("grade : D")
    else:
        if score <=69:
            print("grade : C")
        else:
            if score <=79:
                print("grade : B")
            else:
                if score<=100:
                    print("grade : A")