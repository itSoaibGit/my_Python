favColor = input("What's your Favorite color?\n")

match favColor:
    case "Red":
        color = f"You Favorite color is {favColor}"
    case "Green":
        color = f"You Favorite color is {favColor}"
    case "Blue":
        color = f"You Favorite color is {favColor}"
    case "Yellow":
        color = f"You Favorite color is {favColor}"
    case _:
        color = f"You Favorite color isn't available"

print(color)