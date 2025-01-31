def main():
    result = value(input("Greeting: "))
    print(result)


def value(greeting):
    greeting = greeting.lower()  # Make case-insensitive

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
