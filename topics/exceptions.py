# Syntax error
# print("hello world)


# number.py example
# ValueError - what if user types in a string?
# The problem with this approach is that therem might be other errors so a
# good practice would be to try to think about all possible errors proactively
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")


# second more compact option of same thing but in function
def return_int():
    try:
        return int(input("What's x? "))
    except ValueError:
        print("x is not an integer")


# third option is to just pass the error it will loop but no explanations given
def pass_int():
    try:
        return int(input("What's x? "))
    except ValueError:
        pass
