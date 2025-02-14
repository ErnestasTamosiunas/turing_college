import re


name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last, first = matches.groups()
    name = matches.group(2) + " " + matches.group(1)
    name = f"{first} {last}"
print(f"Hello, {name}!")
