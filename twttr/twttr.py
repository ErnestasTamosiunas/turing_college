def main():
    print(shorten(input("Input: ")))


def shorten(user_input):
    vowels = ("a", "e", "i", "o", "u")
    output = ""
    for chr in user_input:
        if chr.lower() not in vowels:
            output += chr

    return output


if __name__ == "__main__":
    main()
