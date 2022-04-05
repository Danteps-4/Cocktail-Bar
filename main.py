from requests import get
from pprint import PrettyPrinter
from tabulate import tabulate

BASE_URL = "www.thecocktaildb.com/api/json/v1/1/"

printer = PrettyPrinter()

def get_cocktail_by_name(name):
    drinks = get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + name).json()["drinks"]
    # printer.pprint(drinks)

    if drinks:
        if len(drinks) > 1:
            print(f"There are a lot of {name.capitalize()}")
            for i, drink in enumerate(drinks):
                print(f"{i + 1} - {drink['strDrink']}")
            option = 0
            while option <= 0 or option > len(drinks):
                option = int(input(f"Select an option of {name.capitalize()}: "))

                if option > 0 and option <= len(drinks):
                    print()
                    print(f"{drinks[option-1]['strDrink']}".center(40, "-"))
                    print(f"{drinks[option-1]['strAlcoholic']}")
                    get_ingredients(drinks[option-1])
                    print(f"Instructions: {drinks[option-1]['strInstructions']}")
                    print(f"Image preview: {drinks[option-1]['strDrinkThumb']}")

        else:
            print()
            print(f"{drinks[0]['strDrink']}".center(40, "-"))
            print(f"{drinks[0]['strAlcoholic']}")
            get_ingredients(drinks[0])
            print(f"Instructions: {drinks[0]['strInstructions']}")
            print(f"Image preview: {drinks[0]['strDrinkThumb']}")
    else:
        print(f"Does not exist a drink with the name {name}")

def get_random_cocktail():
    random = get("https://www.thecocktaildb.com/api/json/v1/1/random.php").json()["drinks"]
    # printer.pprint(random)

    print(f"{random[0]['strDrink']}".center(40, "-"))
    print(f"{random[0]['strAlcoholic']}")
    get_ingredients(random[0])
    print(f"Instructions: {random[0]['strInstructions']}")
    print(f"Image preview: {random[0]['strDrinkThumb']}")

def get_ingredients(drink):
    # printer.pprint(drink)
    ingredients = []
    for i in range(15):
        if drink[f"strIngredient{i+1}"] is not None and len(drink[f"strIngredient{i+1}"]) != 0:
            ingredient = drink[f"strIngredient{i+1}"]
            measure = drink[f"strMeasure{i+1}"]
            ingredients.append([ingredient, measure])

    print(tabulate(ingredients, headers=["Ingredient", "Measure"], tablefmt="fancy_grid"))


def menu(opt):
    print()
    print("COCKTAIL BAR".center(30, "-"))
    print("1- Get cocktail by name")
    print("2- Get random cocktail (I'm feeling lucky)")
    print("3- Exit")
    opt = int(input("Enter an option: "))

    return opt

option = 0

while option != 3:
    option = menu(option)
    if option == 1:
        name = input("Enter name of a cocktail: ")
        get_cocktail_by_name(name)
    if option == 2:
        get_random_cocktail()
    elif option == 3:
        print("Closing bar program...")
    else:
        print("Invalid option. Please enter a valid option")