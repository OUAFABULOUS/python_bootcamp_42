
import sys
import string

# cookbook = {str: {"ingredients":[], "meal": str, "prep_time": int}}
def	fill_recipe_dict(ingredients, type_meal, prep_time):
    return({"ingredients":ingredients, "meal": type_meal, "prep_time": prep_time})

def	print_details(dict):
    print(f"Ingrediens list:", dict["ingredients"])
    print(f"To be eaten for", dict["meal"])
    print(f"Takes", dict["prep_time"], "minutes of cooking")

def	print_recipe_names(dict):
    for i in range(len(dict)):
        print(list(dict.keys())[i])

def	print_recipe_details(dict, recipe):
    print("RECIPE: ", end="")
    print(recipe.upper())
    print_details(dict[recipe])

def	delete_recipe(dict, recipe):
    del(dict[recipe])

def	add_recipe_from_input(dict):
    name = None
    while name == None or type(name) != str:
        name = input("Recipe's Name: \n")
    ingredients = []
    print("Ingredients of the recipe:")
    while len(ingredients) == 0 or ingredients[len(ingredients) - 1] != "":
        ingredients.append(input())
    type_meal = input("Type of meal: \n")
    time = input("Preparation time: \n")
    cookbook.update({name : fill_recipe_dict(ingredients, type_meal,time)})

if __name__== "__main__":
    cookbook = {"Sandwich" : fill_recipe_dict(["ham", "bread", "cheese", "tomatoes"], "lunch", 10)}
    cookbook.update({"Cake" : fill_recipe_dict(["flour", "sugar", "eggs"],"dessert",60)})
    cookbook.update({"Salad" : fill_recipe_dict(["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15)})
    print("Welcome to the Pyhton Cookbook !")
    print("List of available options:")
    print("	1: Add a recipe")
    print("	2: Delete a recipe")
    print("	3: Print a recipe")
    print("	4: Print the cookbook")
    print("	5: Quit")
    while True:
         option = None
         while option == None or int(option) < 1 or int(option) > 5:
             option = input("Please select an option:\n")
         if int(option) == 1:
             add_recipe_from_input(cookbook)
         elif int(option) == 2:
             recipe = input("The name of the recipe you want to delete: ")
             delete_recipe(cookbook, recipe)
         elif int(option) == 3:
             recipe = input ("The name of the recipe you want to print: ")
             print_recipe_details(cookbook, recipe)
         elif int(option) == 4:
             for i in range(len(cookbook)):
                 print_recipe_details(cookbook, list(cookbook.keys())[i])
         else:
             print("Cookbook closed. Goodbye !")
             exit(1)


