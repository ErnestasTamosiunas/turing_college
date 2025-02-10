import random


def main():
    print(guess())


def guess():
    random_number = 0
    while True:
        if random_number == 0:
            user_input = input("Level: ")
            if user_input.isdigit() and int(user_input) > 0:
                random_number = random.randint(1, int(user_input))
            else:
                continue
        else:
            user_answer = input("Guess: ")
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if user_answer == random_number:
                    return "Just right!"
                elif user_answer > random_number:
                    print("Too large!")
                else:
                    print("Too small!")


if __name__ == "__main__":
    main()
