import requests
import sys


def main():
    input = user_input()
    api_call()
    print(get_result(api_call(), input))


def user_input():
    user_input = sys.argv
    if len(user_input) < 2:
        sys.exit("Missing command-line argument")
    elif not user_input[1].isdigit():
        try:
            return float(user_input[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    return float(user_input[1])


def api_call():
    address = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        r = requests.get(address)
    except requests.RequestException:
        sys.exit("Error while taking request")
    else:
        return r.json()


def get_result(json, input):
    use_case = ["bpi", "USD", "rate"]
    amount = json[use_case[0]][use_case[1]][use_case[2]]
    number = float(amount.replace(",", ""))
    result = number * input
    return f"${result:,.4f}"


if __name__ == "__main__":
    main()
