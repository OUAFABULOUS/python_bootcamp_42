class recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        if type(name) is not str or type(recipe_type) is not str or (recipe_type is not "starter" and recipe_type is not "lunch" and recipe_type is not "dessert"):
            print("Name of the recipe and Recipe type should be a string!")
            quit
        if not type(cooking_lvl)==int or not type(cooking_time)==int or cooking_time < 0 or cooking_lvl < 1 or cooking_lvl > 5:
            print("Cooking level and cooking time should be positive integers! NB cooking level ranges from 1 to 5")
            quit
        if not type(ingredients) is list or len(ingredients) == 0 or not all(isinstance(item,str) for item in ingredients):
            print("Introduce a list of ingredients. They all should be strings")
            quit
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = "Recipe Name: " + self.name + "\nCooking level: " + str(self.cooking_lvl) + "\nIngredients: " + str(self.ingredients) + "\nDescription: " + self.description + "\nRecipe_type: " + self.recipe_type
        return txt

