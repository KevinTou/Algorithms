#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Recipe is {}
    # Ingredients is {}

    # Verify you have all the ingredients
    count = 0

    for key in recipe:
        if key in ingredients:
            count += 1

    batches = 0
    numOfBatches = [0] * count

    # If you have all the ingredients
    index = 0
    if count == len(recipe.keys()):
        # Get the number of batches per ingredient
        for key, value in recipe.items():
            numOfBatches[index] = ingredients[key] // recipe[key]
            index += 1
        # print("Batches: ", numOfBatches)
        x = 0
        while True:
            if x == count:
                batches += 1
                x = 0
            if numOfBatches[x] == 0:
                break
            else:
                numOfBatches[x] -= 1
                x += 1
            # print(numOfBatches)
        return batches
    # If you're missing ingredients, the number of batches is 0
    else:
        return batches


print(recipe_batches({'milk': 100, 'butter': 50, 'flour': 5},
                     {'milk': 138, 'butter': 52, 'flour': 51}))

# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
