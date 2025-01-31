def main():
    print(deep(input("What is the Asnwer to the Great Question of Life, the Universe, and Everything? ")))

def deep(user_input):
    expected_values = {'42', 'forty-two', 'forty two'}
    if user_input.lower().strip() in expected_values:
        return "Yes"
    return "No"

main()