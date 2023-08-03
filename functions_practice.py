def hello():
    print("Hello")

def pack(x, y, z):
    my_list = [x, y, z]
    print(my_list)

pack("fruit","water","soda")


def eat_lunch(lunchbox):
    if len(lunchbox) == 0:
        print("My lunchbox is empty!")

    for index, value in enumerate(lunchbox):
        if index == 0:
            print("First I eat" + value)
        else:
            print("Next I eat " + value)

eat_lunch(["Pizza", "Sandwich", "Steak", "Fish", "Cake"])

eat_lunch([])