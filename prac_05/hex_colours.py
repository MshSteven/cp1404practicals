COLOR_TO_HEX = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc"}
print(COLOR_TO_HEX)

color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        print(color_name, "is", COLOR_TO_HEX[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()

max_length = max(len(hex_color) for hex_color in list(COLOR_TO_HEX.keys()))
for color_name, hex_color in COLOR_TO_HEX.items():
    print(f"{color_name:{max_length}} is {hex_color}")
