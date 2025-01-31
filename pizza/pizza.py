from tabulate import tabulate
import sys
import os
import csv


def main():
    if validate_input(sys.argv):
        print(build_table(prepare_data(sys.argv[1])), end="")


def validate_input(args):
    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    elif not args[1].endswith(".csv"):
        sys.exit("Not a Python file")
    elif not os.path.isfile(f"./{args[1]}"):
        sys.exit("File does not exist")
    return True


def prepare_data(arg):
    data = []
    with open(arg) as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        if headers and len(headers) >= 3:
            header_1, header_2, header_3 = headers[:3]
        else:
            header_1 = header_2 = header_3 = None
        for row in reader:
            data.append(
                {
                    f"{header_1}": row[f"{header_1}"],
                    f"{header_2}": row[f"{header_2}"],
                    f"{header_3}": row[f"{header_3}"],
                }
            )
    return data


def build_table(data):
    headers = data[0].keys()
    rows = [x.values() for x in data]
    return tabulate(rows, headers, tablefmt="grid")


if __name__ == "__main__":
    main()
