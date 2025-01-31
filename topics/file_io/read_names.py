# with open("names.txt", "r") as file:
#    #    lines = file.readlines()
#    #
#    # for line in lines:
#    #    print("Hello,", line.rstrip())
#    for line in file:
#        print("Hello,", line.rstrip())


# names = []
#
# with open("names.txt") as file:
#    for line in file:
#        names.append(line.rstrip())
#
# for name in sorted(names):
#    print(f"Hello, {name}")


with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print(f"Hello, {line.rstrip()}")
