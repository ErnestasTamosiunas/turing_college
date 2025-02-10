import emoji


def main():
    print(translate_into_emoji(input("Input: ")))


def translate_into_emoji(user_input):
    return emoji.emojize(user_input, language="alias")


if __name__ == "__main__":
    main()
