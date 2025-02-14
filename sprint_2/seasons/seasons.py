from datetime import date, datetime
import sys
import inflect


def main() -> None:
    user_input = input("Date of Birth: ").strip()
    result = age_to_minutes(user_input)
    print(result)


def validate_dob(dob: str):
    # Valid date = 1999-01-01
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
        return birth_date
    except ValueError:
        sys.exit()


def age_to_minutes(birth_date):
    today = date.today()
    result = today - birth_date
    return result.days() * 24 * 60


def convert_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    return " ".join(words).capitalize()


if __name__ == "__main__":
    main()
