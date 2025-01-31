import sys
from pyfiglet import Figlet
from random import choice


def main():
    figlet = Figlet()
    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")
    elif sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    print(transform_string(input("Input: "), sys.argv, figlet))


def transform_string(user_input, args, figlet):
    if len(args) == 3:
        figlet.setFont(font=args[2])
        return figlet.renderText(user_input)
    elif len(args) == 1:
        random_font = choice(figlet.getFonts())
        figlet.setFont(font=random_font)
        return figlet.renderText(user_input)

    sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
