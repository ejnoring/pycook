#Final project for Programming for Network Admins
import os
import time

level_content = {
        '1': {
            'pantry': ['instant ramen', 'chef boyardee', 'potato'],
            'fridge': ['water', 'chocolate milk', 'pepsi'],
            'correct_cooker': 'stove',
            'correct_recipe': ['instant_ramen', 'water'],
            'min_cook_time': 2,
            'max_cook_time': 4,
            'name': 'Instant Ramen'
        },
        '2': {
            'pantry': ['instant ramen', 'chef boyardee', 'potato'],
            'fridge': ['water', 'chocolate milk', 'pepsi'],
            'correct_cooker': 'stove',
            'correct_recipe': [],
            'min_cook_time': 2,
            'max_cook_time': 5,
            'name': 'Cheeks'
        }
    }

def update_pantry(item, inventory):
        pantry.remove(item)
        inventory.append(item)
        print('You take the ' + item)

def update_fridge(item, inventory):
        fridge.remove(item)
        inventory.append(item)
        print('You take the ' + item)

def cook_job(inventory, level):
        ingreds = []
        item_to_cook = ''
        cooker = input('What would you like to cook on, stove or oven? ').lower()
        if cooker == 'stove' or cooker == 'oven':
            dish_success = False
            while item_to_cook != 'back' and not dish_success:
                item_to_cook = input("What ingredients would you like to put in the pan? Enter one at a time. Type 'cook' to begin cooking. ").lower()
                if item_to_cook in inventory:
                    ingreds.append(item_to_cook)
                    print('You have put', item_to_cook, 'in the pan.')
                elif item_to_cook == 'cook':
                    cooktime = ''
                    while cooktime != 'back' and not dish_success:
                        cooktime = input('How long would you like to cook your dish for? (in minutes) ')
                        if cooker == level_content[str(level)]['correct_cooker']:
                            if int(cooktime)  < level_content[str(level)]['max_cook_time'] and int(cooktime) > level_content[str(level)]['min_cook_time']:
                                print("The dish is successful.")
                                dish_success = True
                            elif int(cooktime) > level_content[str(level)]['max_cook_time']:
                                print('The dish is burnt! Try again.')
                            else:
                                print('The dish is undercooked. Try again.')
                        else:
                            print('Incorrect cooker.')
                else:
                    print("You don't have " + item_to_cook + '.')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
print('''Pycook is a text-based cooking game written in Python.
Players take the role of a personal chef cooking for VIP clients. As the game progresses, the dishes gradually become more difficult.\n\n
Players will start each level at the kitchen counter. From here you may access the fridge where you'll find your cold ingredients,
the pantry where you'll find spices/seasonings along with your cooking utensils, and the cook space which includes a stovetop and oven.\n\n
The chef must use his or her own intuition to choose the proper ingredients, seasonings, and cook times for each of the dishes.
If the chef ruins the dish, they will be allowed up to 5 attempts to remake the dish. If the dish is not properly made in 5 attempts, the chef will be fired.
A chef who is fired must start from level 1 and work his or her way back up to earn the respect of the clients.\n''')

play = input('Press enter to begin.')
if play == '':
    pass
else:
    pass

clear()
max_level = 20
level = 1

while level < max_level:
    inventory = []
    fridge = level_content[str(level)]['fridge']
    pantry = level_content[str(level)]['pantry']
    cook_space = ['stove', 'oven']
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
                else:
                    print("That item doesn't exist.")
        elif loc == 'cook space':
            cook_job(inventory, level)
            level += 1
            in_progress = False
            time.sleep(3)
            clear()
