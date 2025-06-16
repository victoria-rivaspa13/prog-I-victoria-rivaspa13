from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    clean_ingredients_set = set(dish_ingredients)
    return (dish_name, clean_ingredients_set)

def check_drinks(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"




