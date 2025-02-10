import sys
import os
import csv


def main():
    if validate_input(sys.argv):
        prepared_data = prepare_data(sys.argv[1])
        build_csv(prepared_data, sys.argv[2])


def validate_input(args):
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    elif not args[1].endswith(".csv") and not args[2].endswith(".csv"):
        sys.exit("Not a .csv file")
    elif not os.path.isfile(f"./{args[1]}"):
        sys.exit("File does not exist")
    return True


def prepare_data(arg):
    data = []
    with open(arg) as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        if headers and len(headers) == 2:
            header_1, header_3 = headers[:2]
        else:
            header_1 = header_3 = None
        for row in reader:
            last_name, name = row[header_1].split(",")
            name = name.lstrip()
            data.append(
                {
                    "first": name,
                    "last": last_name,
                    f"{header_3}": row[header_3],
                }
            )
    return data


def build_csv(data, file_name):
    with open(file_name, "w") as file:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(
                {
                    fieldnames[0]: row[fieldnames[0]],
                    fieldnames[1]: row[fieldnames[1]],
                    fieldnames[2]: row[fieldnames[2]],
                }
            )


if __name__ == "__main__":
    main()
