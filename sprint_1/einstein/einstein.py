def kilograms_to_joules(kilograms):
    joule = 90000000000000000
    return int(kilograms) * joule

def main():
    user_input = input()
    print(kilograms_to_joules(user_input))

main()