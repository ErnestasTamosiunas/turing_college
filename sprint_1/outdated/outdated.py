def main():
    print(convert_date(), end="")


def convert_date():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        try:
            user_input = input("Date: ").strip()

            if "," in user_input and user_input[:1].isalpha():
                user_input = user_input.replace(",", "")
                month, day, year = user_input.split(" ")
                day = int(day)
                year = int(year)
                if month in months and 1 <= day <= 31 and len(str(year)) == 4:
                    return f"{year}-{months.index(month) + 1:02}-{day:02}"

            elif "/" in user_input and user_input[:1].isdigit():
                month, day, year = map(int, user_input.split("/"))
                if 1 <= month <= 12 and 1 <= day <= 31 and len(str(year)) == 4:
                    return f"{year}-{month:02}-{day:02}"

        except Exception:
            pass


if __name__ == "__main__":
    main()
