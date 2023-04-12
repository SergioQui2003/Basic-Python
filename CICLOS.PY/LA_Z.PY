def print_Z():
    for i in range(5):
        if i == 0 or i == 4:
            print("*****")
        else:
            print("*")
            for j in range(4-i):
                print(" ", end="")
            print("*")

print_Z()