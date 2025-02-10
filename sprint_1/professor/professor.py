import random


def main():
    chosen_level = get_level()
    score = 0
    for i in range(0, 10):
        x = generate_integer(chosen_level)
        y = generate_integer(chosen_level)

        expected_result = str(x + y)
        failed_attempts = 0
        while True:
            addition = f"{x} + {y} = "
            user_answer = input(f"{i + 1}: {addition}")
            if user_answer.isdigit():
                if user_answer == expected_result and user_answer.isdigit():
                    score += 1
                    break
                else:
                    if failed_attempts == 2:
                        print("EEE")
                        print(addition + expected_result)
                        break
                    else:
                        failed_attempts += 1
                        print("EEE")
                        continue

    print(f"Score: {score}")


def get_level():
    while True:
        user_input = input("Level: ")
        if user_input.isdigit() and 0 < int(user_input) <= 3:
            return int(user_input)
        else:
            continue


def generate_integer(level):
    level_range = {1: [0, 10], 2: [10, 99], 3: [100, 999]}
    return random.randrange(level_range[level][0], level_range[level][1])


if __name__ == "__main__":
    main()
