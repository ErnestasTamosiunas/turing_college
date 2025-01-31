import sys


def main():
    grocery_app()


def grocery_app():
    grocery_dict = {}

    while True:
        try:
            user_input = input().upper()
        except EOFError:
            grocery_dict = dict(sorted(grocery_dict.items()))
            for item in grocery_dict:
                print(f"{grocery_dict[item]} {item}")
            sys.exit(0)
        else:
            if user_input not in grocery_dict:
                grocery_dict[user_input] = 1
            else:
                grocery_dict[user_input] = grocery_dict[user_input] + 1


if __name__ == "__main__":
    main()
