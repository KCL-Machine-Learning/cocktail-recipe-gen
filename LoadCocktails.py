import pandas as pd

#Loads the recipes from csv file in the same directory
def loadData():
    print("Loading cocktail recipes...")
    all_recipesCSV = pd.read_csv("cocktail_recipes.csv")


    all_recipes = []
    #Loads the recipes row by row into an array of arrays
    for i, recipeCSV in all_recipesCSV.iterrows():
        recipe = list(recipeCSV)
        all_recipes.append(recipe)

    print("Recipes loaded!")
    return all_recipes


