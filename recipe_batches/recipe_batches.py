#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    recipe_ingredients = [k for k, v in recipe.items()]
    ingredients_available = [k for k, v in ingredients.items()]
    for elem in recipe_ingredients:
        if elem not in ingredients_available:  # recipe ingredient not in our ingredients
            return 0

    mults = {k: 0 for k, v in recipe.items()}
    for k, v in recipe.items():
        mults[k] = ingredients[k]//recipe[k]
    return min([v for k, v in mults.items()])


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
