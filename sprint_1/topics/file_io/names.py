name = input("What's your name? ")

# w = open new file and overrwrite if anything else existed good for start
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
