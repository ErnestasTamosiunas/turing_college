def main():
    print(interpreter(input("Expression: ")))


def multiply(x, y):
    return x * y


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return round(x / y, 1)


def to_float(string):
    return float(string)


def interpreter(user_input):
    x, y, z = user_input.split(" ")
    x = to_float(x)
    z = to_float(z)
    if y == "*":
        return multiply(x, z)
    if y == "+":
        return add(x, z)
    if y == "-":
        return subtract(x, z)
    if y == "/":
        return divide(x, z)


main()
