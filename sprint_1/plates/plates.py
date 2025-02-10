def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(user_input):
    if len(user_input) < 2 or len(user_input) > 6:
        return False
    if not user_input[0:2].isalpha():
        return False
    was_digit = False
    for c in user_input[2:]:
        if c.isdigit() and was_digit is False:
            if int(c) == 0:
                return False
            was_digit = True
        if not c.isdigit() and was_digit is True:
            return False
        if not c.isdigit() and not c.isalpha():
            return False

    return True


if __name__ == "__main__":
    main()
