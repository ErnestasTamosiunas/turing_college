import inflect


def main():
    print(adieu())


def adieu():
    p = inflect.engine()
    name_list = []
    result = "Adieu, adieu, to "
    while True:
        try:
            name_list.append(input("Name: "))
        except EOFError:
            if len(name_list) == 1:
                return result + name_list[0]
            else:
                return result + p.join(name_list)


if __name__ == "__main__":
    main()
