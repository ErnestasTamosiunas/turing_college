def main():
    print(coke_machine())


def coke_machine():
    acceptable_coins = (25, 10, 5)
    amount_left = 50
    while True:
        user_input = int(input("Insert Coin: "))
        if user_input in acceptable_coins:
            amount_left -= user_input

        if amount_left <= 0:
            return f"Change Owed: {abs(amount_left)}"
        else:
            print(f"Amount Due: {amount_left}")


if __name__ == "__main__":
    main()
