

class book:

    def __str__(self):
        txt = "Recipe Name: {name}\nCooking level: {cooking_lvl}\nIngredients: {ingredients}\nDescription: {description}\nRecipe_type: {recipe_type}"
        return txt

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        if type(name) is not str or type(recipe_type) is not str:
            print("Name of the recipe and Recipe type should be a string!")
            quit
        if not cooking_lvl.isdigit() or not cooking_time.isdigit() or cooking_time < 0 or cooking_lvl < 0:
            print("Cooking level and cooking time should be positive integers!")
            quit
        if not type(ingredients) is list or len(list) == 0 or not all(isinstance(item,str) for item in ingredients):
            print("Introduce a list of ingredients. They all should be strings")
            quit
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.descrption = description
        self.recipe_type = recipe_type
