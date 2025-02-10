def main():
    user_input = input("Fraction: ")
    result = gauge(convert(user_input))
    print(result)


def convert(fraction):
    numerator, denominator = map(int, fraction.split("/"))
    if denominator == 0:
        raise ZeroDivisionError
    if numerator > denominator or numerator < 0:
        raise ValueError
    return round((numerator / denominator) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
