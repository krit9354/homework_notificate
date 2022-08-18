def show_info():
    print("Calculate circumference and area of a circle")


def input_data():
    return float(input("diameter :")) / 2


def cal_circum(radius):
    return 2 * 3.14 * radius


def cal_area(radius):
    return 3.14 * (radius ** 2)


def show(circum, area):
    print("circumference =", circum)
    print("area of a circle =", area)


def main():
    show_info()
    raduis = input_data()
    circum = cal_circum(raduis)
    area = cal_area(raduis)
    show(circum, area)


main()
