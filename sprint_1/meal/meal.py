meal_dictionary = {"breakfast": [7, 8], "lunch": [12, 13], "dinner": [18, 19]}


def main():
    print(meal_matcher(convert(input("What time is it? "))))


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(int(minutes) / 6) / 10


def meal_matcher(t):
    get_after_decimal = round(t % 1, 2)
    minutes = int(get_after_decimal * 10)
    hours = int(t - get_after_decimal)
    for meal in meal_dictionary:
        result = f"{meal} time"
        if hours == meal_dictionary[meal][0] and minutes < 60:
            return result
        if hours == meal_dictionary[meal][1] and minutes == 0:
            return result


if __name__ == "__main__":
    main()
