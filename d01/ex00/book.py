from datetime import datetime
from recipe import recipe

def check_recipes_dict(recipes_list):
    if type(recipes_list) is not dict or len(recipes_list) is not 3 or list(recipes_list.keys())[0] is not "starter" or list(recipes_list.keys())[1] is not "lunch" or list(recipes_list.keys())[2] is not "dessert":
        if type(recipes_list["starter"]) is not list or type(recipes_list["lunch"]) is not list or type(recipes_list["dessert"]) is not list:
            return 1
    return 0


class book:
    def	__init__(self, name, recipes_list={"starter": {}, "lunch" : {} , "dessert": {}}):
        if type(name) is not str or check_recipes_dict(recipes_list):
            print("Name should be a string.\nRecipe list should be a dictionnary with the 3 keys: starter, lunch, dinner")
            quit
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipes_list = recipes_list

    def	get_recipes_by_types(self, recipe_type):
        for j in range(len(self.recipes_list[recipe_type])):
            print(self.recipes_list[recipe_type][j].__str__())
                # return self.recipes_list[list(self.recpes_list.list)[i]][j].__str__()

    def	get_recipe_by_name(self, name):
        print((self.recipes_list["starter"][name]).__str__())
        print((self.recipes_list["lunch"][name]).__str__())
        print((self.recipes_list["dessert"][name]).__str__())

    def	add_recipe(self, recipe):
        self.recipes_list[recipe.recipe_type] = recipe
        self.last_update = datetime.now()

