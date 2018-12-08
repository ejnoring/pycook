# Final project for Programming for Network Admins
# Pycook
import os
import time

# Level content contains the data for all 20 levels of the game.
level_content = {
        '1': {
            'pantry': ['instant ramen', 'chef boyardee', 'potato'],
            'fridge': ['water', 'chocolate milk', 'pepsi'],
            'correct_cooker': 'stove',
            'correct_recipe': ['instant ramen', 'water'],
            'min_cook_time': 2,
            'max_cook_time': 4,
            'name': 'Instant Ramen'
        },
        '2': {
            'pantry': ['macaroni', 'stuffing', 'beef jerky', 'cheese'],
            'fridge': ['water', 'apple juice', 'eggs'],
            'correct_cooker': 'stove',
            'correct_recipe': ['cheese', 'macaroni', 'water'],
            'min_cook_time': 6,
            'max_cook_time': 10,
            'name': 'Kraft Mac'
        },
        '3': {
            'pantry': ['ketchup', 'onion', 'garlic'],
            'fridge': ['fish sticks', 'chicken strips'],
            'correct_cooker': 'oven',
            'correct_recipe': ['fish sticks'],
            'min_cook_time': 10,
            'max_cook_time': 15,
            'name': 'Fish Sticks'
        },
        '4': {
            'pantry': ['soy sauce', 'creamed corn', 'bread'],
            'fridge': ['almond milk', 'cheese', 'butter'],
            'correct_cooker': 'stove',
            'correct_recipe': ['bread', 'butter', 'cheese'],
            'min_cook_time': 2,
            'max_cook_time': 4,
            'name': 'Grilled Cheese'
        },
        '5': {
            'pantry': ['canned soup', 'carrots'],
            'fridge': ['eggs', 'vegetable tray'],
            'correct_cooker': 'stove',
            'correct_recipe': ['eggs'],
            'min_cook_time': 1,
            'max_cook_time': 2,
            'name': 'Sunny Side Up Eggs'
        },
        '6': {
            'pantry': ['breadcrumb', 'hot sauce', 'grass', 'spaghetti'],
            'fridge': ['cheese', 'ground beef', 'mayo', 'water', 'eggs'],
            'correct_cooker': 'stove',
            'correct_recipe': ['breadcrumb', 'eggs', 'ground beef', 'spaghetti', 'water'],
            'min_cook_time': 6,
            'max_cook_time': 10,
            'name': 'Spaghetti and Meatballs'
        },
        '7': {
            'pantry': ['hamburger buns', 'hotdog buns', 'soy sauce'],
            'fridge': ['chicken breast', 'beef patty', 'cheese', 'asparagus'],
            'correct_cooker': 'stove',
            'correct_recipe': ['beef patty', 'cheese', 'hamburger buns'],
            'min_cook_time': 5,
            'max_cook_time': 8,
            'name': 'Cheeseburger'
        },
        '8': {
            'pantry': ['cookies', 'lasanga sheets', 'beans', 'tomato sauce'],
            'fridge': ['ground beef', 'mozzarella', 'Hy-Vee Cola'],
            'correct_cooker': 'oven',
            'correct_recipe': ['ground beef', 'lasagna sheets', 'mozzarella', 'tomato sauce'],
            'min_cook_time': 10,
            'max_cook_time': 15,
            'name': 'Lasagna'
        },
        '9': {
            'pantry': ['mayo', 'taco shells', 'butter'],
            'fridge': ['ground beef', 'tomato', 'brown gravy', 'cheese'],
            'correct_cooker': 'stove',
            'correct_recipe': ['cheese', 'ground beef', 'taco shells', 'tomato'],
            'min_cook_time': 5,
            'max_cook_time': 8,
            'name': 'Tacos'
        },
        '10': {
            'pantry': ['chili powder', 'beef broth', 'corn nuts', 'beans', 'onion', 'book'],
            'fridge': ['lettuce', 'ground beef', 'strawberry', 'tomato'],
            'correct_cooker': 'stove',
            'correct_recipe': ['beans', 'beef broth', 'chili powder', 'ground beef', 'onion', 'tomato'],
            'min_cook_time': 15,
            'max_cook_time': 30,
            'name': 'Chili'
        },
        '11': {
            'pantry': ['potato', 'onion', 'wheat', 'rice', 'soy sauce', 'english muffin'],
            'fridge': ['peas', 'carrots', 'eggs', 'green onion'],
            'correct_cooker': 'stove',
            'correct_recipe': ['carrots', 'eggs', 'green onion', 'onion', 'peas', 'rice', 'soy sauce'],
            'min_cook_time': 10,
            'max_cook_time': 15,
            'name': 'Fried Rice'
        },
        '12': {
            'pantry': ['sugar', 'brown sugar', 'chili powder', 'flour', 'cumin', 'baking soda', 'vanilla'],
            'fridge': ['butter', 'eggs', 'ribeye' , 'chocolate chips'],
            'correct_cooker': 'oven',
            'correct_recipe': ['baking soda', 'brown sugar', 'butter', 'chocolate chips', 'eggs', 'flour', 'vanilla'],
            'min_cook_time': 13,
            'max_cook_time': 18,
            'name': 'Chocolate Chip Cookies'
        },
        '13': {
            'pantry': ['chicken broth', 'corn syrup', 'pumpkin pie spice', 'onion', 'vegetable broth', 'egg noodles', ],
            'fridge': ['celery', 'chicken', 'orange juice' , 'carrots', 'Dr. Pepper'],
            'correct_cooker': 'stove',
            'correct_recipe': ['carrots', 'celery', 'chicken', 'chicken broth', 'eggs noodles', 'onion', 'vegetable broth'],
            'min_cook_time': 20,
            'max_cook_time': 40,
            'name': 'Chicken Noodle Soup'
        },
        '14': {
            'pantry': ['onion', 'carrots', 'honey', 'corn', 'cake mix'],
            'fridge': ['chicken breast', 'mushrooms', 'butter', 'chicken wings', 'milk'],
            'correct_cooker': 'stove',
            'correct_recipe': ['butter', 'chicken breast', 'mushrooms', 'onion'],
            'min_cook_time': 10,
            'max_cook_time': 14,
            'name': 'Smothered Chicken'
        },
        '15': {
            'pantry': ['onion', 'apples', 'A1' 'fajita seasoning'],
            'fridge': ['bell peppers', 'tortillas', 'romaine lettuce', 'steak', 'New Hampshire'],
            'correct_cooker': 'stove',
            'correct_recipe': ['bell pepper', 'fajita seasoning', 'onion', 'steak', 'tortilla'],
            'min_cook_time': 7,
            'max_cook_time': 11,
            'name': 'Steak Fajitas'
        },
        '16': {
            'pantry': ['onion', 'potato', 'banana', 'Grey Poupon', 'applesauce'],
            'fridge': ['bacon', 'water', 'La Croix', 'eggs', 'bell peppers', 'tortillas'],
            'correct_cooker': 'stove',
            'correct_recipe': ['bacon', 'bell pepper', 'eggs', 'onion', 'potato', 'tortilla'],
            'min_cook_time': 8,
            'max_cook_time': 12,
            'name': 'Breakfast Burrito'
        },
        '17': {
            'pantry': ['bread', 'sugar', 'flour', 'onion', 'butter', 'hot sauce'],
            'fridge': ['water', 'eggs', 'shrimp', 'milk'],
            'correct_cooker': 'oven',
            'correct_recipe': ['bread', 'butter', 'egg', 'milk', 'sugar'],
            'min_cook_time': 20,
            'max_cook_time': 30,
            'name': 'Bread Pudding'
        },
        '18': {
            'pantry': ['doritos', 'peanut butter', 'english muffin', 'nuetella', 'Bisquick'],
            'fridge': ['hollandaise sauce', 'eggs', 'water'],
            'correct_cooker': 'stove',
            'correct_recipe': ['eggs', 'english muffin', 'hollandaise sauce', 'water'],
            'min_cook_time': 6,
            'max_cook_time': 7,
            'name': 'Eggs Benedict'
        },
        '19': {
            'pantry': ['pecans', 'peanuts', 'sugar', 'corn syrup', 'molasses', 'brown sugar', 'butter'],
            'fridge': ['pie crust', 'ground beef', 'salsa'],
            'correct_cooker': 'oven',
            'correct_recipe': ['brown sugar', 'butter', 'corn syrup', 'pecans', 'pie crust'],
            'min_cook_time': 40,
            'max_cook_time': 60,
            'name': 'Pecan Pie'
        },
        '20': {
            'pantry': ['chicken stock', 'beef stock', 'vegetable broth', 'egg noodles', 'rice noodles', 'fish sauce', 'onion', 'potato'],
            'fridge': ['beef sirloin', 'ginger', 'water', 'cilantro', 'parsley', 'green onion', 'basil', 'Coca-Cola', 'lettuce'],
            'correct_cooker': 'stove',
            'correct_recipe': ['basil', 'beef sirloin', 'beef stock', 'cilantro', 'fish sauce', 'ginger', 'green onion', 'onion', 'rice noodles', 'water'],
            'min_cook_time': 120,
            'max_cook_time': 600,
            'name': 'Pho'
    }}

# When a player requests an item, run update_pantry or update_fridge to remove the item from the pantry/fridge list and add
# that item to the player's inventory list
def update_pantry(item, inventory):
        pantry.remove(item)
        inventory.append(item)
        print('You take the ' + item)

def update_fridge(item, inventory):
        fridge.remove(item)
        inventory.append(item)
        print('You take the ' + item)
# cook_job contains the cook logic for the game. Players are asked to choose between the oven or the stove. They are then asked what
# ingredients they would like to add to the pan. Ingredients are moved from a player's inventory list into the 'ingreds' list.
# Players are then asked to enter the amount of time they would like to cook their dish for.
# Player's dishes must match the correct_cooker, correct_recipe, and fall between the min and max cook time stated in level_content.
def cook_job(inventory, level):
    ingreds = []
    item_to_cook = ''
    cooker = ''
    global dish_success
    dish_success = False
    while True and not dish_success:
        cooker = input('What would you like to cook on, stove or oven? ').lower()
        if cooker == 'back':
            global retain_inventory
            retain_inventory = True
            break
        item_to_cook = ''
        while not dish_success and item_to_cook != 'back':
            if cooker == 'stove' or cooker == 'oven':
                dish_success = False
                while item_to_cook != 'back' and not dish_success:
                    item_to_cook = input("What ingredients would you like to put in the pan? Enter one at a time. Type 'cook' to begin cooking. ").lower()
                    if item_to_cook in inventory:
                        ingreds.append(item_to_cook)
                        print('You have put', item_to_cook, 'in the pan.')
                    elif item_to_cook == 'help':
                        help()
                    elif item_to_cook == 'cook':
                        cooktime = ''
                        while cooktime != 'back' and not dish_success:
                            cooktime = input('How long would you like to cook your dish for? (in minutes) Type "back" to go back. ')
                            if cooker == level_content[str(level)]['correct_cooker']:
                                ingreds.sort()
                                if ingreds == level_content[str(level)]['correct_recipe']:
                                    if int(cooktime) < level_content[str(level)]['max_cook_time'] and int(cooktime) > level_content[str(level)]['min_cook_time'] and ingreds == level_content[str(level)]['correct_recipe']:
                                        print("The dish is successful.")
                                        dish_success = True
                                        retain_inventory = False
                                    elif int(cooktime) > level_content[str(level)]['max_cook_time']:
                                        print('The dish is burnt! Try again.')
                                    else:
                                        print('The dish is undercooked. Try again.')
                                elif cooktime != 'back' and ingreds != level_content[str(level)]['correct_recipe']:
                                    print('Incorrect ingredients. Try again.')
                            elif cooktime != 'back':
                                print('Incorrect cooking instrument.')
                    elif item_to_cook == 'back':
                        break
                    else:
                        print("You don't have " + item_to_cook + '.')
            else:
                print('Please select either oven or stove.')
                break
# Defined function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# 'Help' can be typed from any menu to display the message explaining how the game works.
def help():
    print()
    print('''Choose ingredients by navigating to the fridge/pantry and typing the ingredients you wish to choose from the list of ingredients.
 Once you have these ingredients, navigate to the cook space, choose your cooker, combine the ingredients and set the time.
 Type 'help' at any time to bring up this message again.''')
    print()


clear()
print('''Pycook is a text-based cooking game written in Python.
Players take the role of a personal chef cooking for VIP clients. As the game progresses, the dishes gradually become more difficult.\n\n
Players will start each level at the kitchen counter. From here you may access the fridge where you'll find your cold ingredients,
the pantry where you'll find dry ingredients and the cook space which will include a stovetop and oven.\n\n
The chef must use his or her own intuition to choose the proper ingredients, seasonings, and cook times for each of the dishes.\n\n''')

play = input('Press enter to begin.')
if play == '':
    pass
else:
    pass

clear()
max_level = 20
level = 1
retain_inventory = False
# Player's inventories, pantries, and fridges are reinitiallized with every level. Players may navigate between the fridge, pantry,
# and cook space to gather items for their dishes and to cook their dishes. If a player cooks their dish, and it meets the criteria
# defined in cook_job, 'level' is incremented by 1 and the loop is reinitiallized with the new data from the next level in level_content
while level < max_level:
    if retain_inventory != True:
        inventory = []
        fridge = level_content[str(level)]['fridge']
        pantry = level_content[str(level)]['pantry']
        cook_space = ['stove', 'oven']
    else:
        continue
    in_progress = True
    print('Level {}: {}'.format(str(level), level_content[str(level)]['name']))
    while in_progress:
        loc = input('You are at the kitchen counter. You see the fridge, pantry, and cook space. Where would you like to go? ')
        if loc == 'fridge':
            while True:
                if len(fridge) > 0:
                    print('In the fridge you see ', fridge, "Type 'back' to return.")
                    cold_item = input('What would you like to take? ').lower()
                else:
                    print('There is nothing in the fridge.')
                    break
                if cold_item in fridge:
                    update_fridge(cold_item, inventory)
                elif cold_item == 'back':
                    break
                elif cold_item == 'help':
                    help()
                else:
                    print("That item doesn't exist.")
        if loc == 'pantry':
            while True:
                if len(pantry) > 0:
                    print('In the pantry you see ', pantry, "Type 'back' to return.")
                    dry_item = input('What would you like to take? ').lower()
                else:
                    print('There is nothing in the fridge.')
                    break
                if dry_item in pantry:
                    update_pantry(dry_item, inventory)
                elif dry_item == 'back':
                    break
                elif dry_item == 'help':
                    help()
                else:
                    print("That item doesn't exist.")
        elif loc == 'help':
            help()
        elif loc == 'cook space':
            cook_job(inventory, level)
            if dish_success == True:
                level += 1
                in_progress = False
                time.sleep(3)
                clear()
            else:
                continue
print('Congratulations! You have beat the game.')
