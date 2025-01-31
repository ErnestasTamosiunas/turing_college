def main():
    print(nutrition_value(input("Item: ")))


def nutrition_value(user_input):
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }
    if user_input.lower() in fruit_calories:
        return f"Calories: {fruit_calories[user_input.lower()]}"
    else:
        return ""


if __name__ == "__main__":
    main()
