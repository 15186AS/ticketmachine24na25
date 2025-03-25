import json

with open("prices.json", "r", encoding="UTF-8") as file:
    prices = json.load(file)

def display_menu(menu):
    print("Jaką opcję biletu chcesz kupić?")
    options = list(menu.keys())
    for index, option in enumerate(options):
        print(f"{index} - {option}")
    try:
        choice = int(input("Wybór: "))
    except ValueError:
        print("Wprowaadzono niepoprawny typ wartości. ")
    if choice > len(options)-1 or choice < 0:
        raise ValueError("Wprowadzono błędny numer opcji.")
    menu = menu[options[choice]]
    if isinstance(menu ,dict):
        return display_menu(menu)
    else:
        return (option, menu)


print(display_menu(prices))