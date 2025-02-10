import sys
import os


def main():
    if validate_input(sys.argv):
        print(count_code_lines(sys.argv[1]), end="")


def validate_input(args):
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    elif not args[1].endswith(".py"):
        sys.exit("Not a Python file")
    elif not os.path.isfile(f"./{args[1]}"):
        sys.exit("File does not exist")
    return True


def count_code_lines(arg):
    line_count = 0
    with open(arg) as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith("#"):
                line_count += 1
    return line_count


if __name__ == "__main__":
    main()
