x = 0
durian = 0
weight = 1
total_weight = 0
while weight !=0:
    x += 1
    weight = int(input("Please input Durian Weight x :"))
    total_weight += weight
print("Total of",x-1,"Durians")
print("Average weight is",total_weight//(x-1))