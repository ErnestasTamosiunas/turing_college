def main():
    print(camel_to_snake(input("camelCase: ")))


def camel_to_snake(input):
    word = ""
    words = []
    for c in input:
        if c.isupper():
            if word:
                words.append(word)
            word = c.lower()
        else:
            word += c

    if word:
        words.append(word)

    return "_".join(words)


if __name__ == "__main__":
    main()
