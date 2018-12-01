#Final project for Programming for Network Admins
import os

# Checks if food_to_find is a valid item for the level. Pantry and fridge are booleans
# Only one should be true when the funciton is called. For example, if pantry is true,
# validate_item will search only for items that will be found in the pantry. If fridge
# is true, validate_item will look for items that only exist in the fridge for the current level
def validate_item(food_to_find, level, pantry = False, fridge = False):
    if pantry:
        return food_to_find in big_food[str(level)]['pantry']
    elif fridge:
        return food_to_find in big_food[str(level)]['fridge']
    return False
        #print(big_food[str(level)]['pantry'])
        # use pantry keys
#return food_to_find in big_food[str(level)]['pantry']

def update_pantry(item, inventory):
        pantry.remove(item)
        inventory.append(item)
        print('You take the ' + item)
def update_fridge(item, inventory):
        fridge.remove(item)
        inventory.append(item)
        print('You take the ' + item)






big_food = {
    '1': {
        'pantry': ['instant ramen', 'chef boyardee', 'potato'],
        'fridge': ['water', 'chocolate milk', 'pepsi']
    },
    #'2': {

    #}
}

os.system('cls' if os.name == 'nt' else 'clear')
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

os.system('cls' if os.name == 'nt' else 'clear')

print('Level 1: Instant Ramen')

while True:
    level = 1
    inventory = []
    fridge = big_food[str(level)]['fridge']
    pantry = big_food[str(level)]['pantry']
    cook_space = ['stove', 'oven']
    loc = input('You are at the kitchen counter. You see the fridge, pantry, and cook space. Where would you like to go? ')
    if loc == 'fridge':
        while True:
            if len(fridge) > 0:
                print('In the fridge you see ', fridge, "Type 'back' to return.")
                cold_item = input('What would you like to take? ').lower()
            else:
                print('There is nothing in the fridge.')
                break
            if validate_item(cold_item, 1, fridge = True):
                update_fridge(cold_item, inventory)
            elif cold_item == 'back':
                break
            else:
                print("That item doesn't exist.")
            
    elif loc == 'cook space':
        while True:
            cooker = input("Would you like to use the oven, or the stove? Type 'back' to return. ").lower()
            if cooker == 'oven':
                ingreds = []
                while True:
                    cooking = input("What ingredients would you like to put in the pan? Enter one at a time. Type 'cook' to begin cooking. ").lower()
                    if cooking in inventory:
                        ingreds.append(cooking)
                        print('You have put', ingreds, 'in the pan.')
                    elif cooking == 'cook':
                        while True:
                            cooktime = input('How long would you like to cook your dish for? (in minutes) ')
                            if int(cooktime)  < 4 and int(cooktime) > 2:
                                print("The dish is successful. I would've used the stove, but it's instant ramen. You can't really mess it up.")
                            elif int(cooktime) > 4:
                                print('The dish is burnt! Try again.')
                            else:
                                print('The dish is undercooked! Try again.')
                    else:
                        print("You don't have " + cooking + '.')
            if cooker == 'stove':
                ingreds = []
                while True:
                    cooking = input("What ingredients would you like to put in the pot? Enter one at a time. Type 'cook' to begin cooking. ").lower()
                    if cooking in inventory:
                        ingreds.append(cooking)
                        print('You have put', ingreds, 'in the pot.')
                    elif cooking == 'cook':
                        while True:
                            cooktime = input('How long would you like to cook your dish for? (in minutes) ')
                            if int(cooktime)  < 4 and int(cooktime) > 2:
                                print("The dish is successful.")
                            elif int(cooktime) > 4:
                                print('The dish is burnt! Try again.')
                            else:
                                print('The dish is undercooked! Try again.')
                    else:
                        print("You don't have " + cooking + '.')
    else:
        print('Nothing happens')
