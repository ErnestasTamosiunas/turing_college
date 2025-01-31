def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input()
    print(convert(user_input))

main()