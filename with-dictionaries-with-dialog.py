'''
Set up the game's size - this is based on the size of the tiles you are using
Each 'tile' is 64x64 pixels
'''
TILE_SIZE = 64
WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 12



'''
Set up the shop background
shop_tiles is a list of all the images that make up the background
shop_map is a list of where each image should go in an x,y grid
'''
shop_tiles = ['floor',
              'bench_corner',
              'bench_bottom',
              'bench_side',
              'wall',
              'textbox']
shop_map = [ [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 2, 2, 2, 1, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 4, 4, 4, 4, 4, 4, 0, 0, 4],
             [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
             [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
             ]



'''
Set up the characters
player and shopkeeper have an image and a start position
player and shopkeeper have a list of the items they are carrying
player and shopkeeper have a dictionary of their stats
till does not have any items, but it is a character so that the player can interact with it
'''
player = Actor('player', anchor=(0, 0), pos=(7 * TILE_SIZE, 8 * TILE_SIZE))
player_items = []
player_stats = {'money': 10, 'energy': 100}

shopkeeper = Actor('shopkeeper', anchor=(0,0), pos=(2 * TILE_SIZE, 3 * TILE_SIZE))
shopkeeper_items = ['oolong tea', 'green tea', 'white tea', 'black tea', 'puerh tea']
shopkeeper_stats = {'money': 50}

till = Actor('till', anchor=(0,0), pos=(2 * TILE_SIZE, 4.5 * TILE_SIZE))



'''
Set what text should be shown at the start, then draw everything onto the screen
1: draw the background, using the tile information given above
2: draw the till, the player, then the shopkeeper in their positions
3: draw the text in the text box, at a set position
'''
shop_text = 'Hello, welcome to my shop! \nCome to the till and press SPACE'
def draw():
    global shop_text
    screen.clear()
    for row in range(len(shop_map)):
        for column in range(len(shop_map[row])):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            tile = shop_tiles[shop_map[row][column]]
            screen.blit(tile, (x, y))
    till.draw()
    player.draw()
    shopkeeper.draw()
    screen.draw.text(shop_text, (0.5 * TILE_SIZE, 10.5 * TILE_SIZE), color="black")



'''
Set up which keyboard buttons can be used by the game
keyboard_variables is a dictionary pairing the key presses with a value - this is useful for keeping track of what you press during the game
keyboard will be set to the last key pressed - it is set to False at the start of the game
'''
keyboard_variables = {keys.UP: 'up', keys.DOWN: 'down', keys.LEFT: 'left', keys.RIGHT: 'right', keys.SPACE: 'space', keys.ESCAPE: 'escape', keys.RETURN: 'return',
                    keys.Y: 'y', keys.N: 'n', keys.I: 'i', keys.S: 's',
                    keys.KP0: 0, keys.KP1: 1, keys.KP2: 2, keys.KP3: 3, keys.KP4: 4, keys.KP5: 5, keys.KP6: 6, keys.KP7: 7, keys.KP8: 8, keys.KP9: 9,
                    keys.K_0: 0, keys.K_1: 1, keys.K_2: 2, keys.K_3: 3, keys.K_4: 4, keys.K_5: 5, keys.K_6: 6, keys.K_7: 7, keys.K_8: 8, keys.K_9: 9}
keyboard = False



'''
Define what happens when you press a key on the keyboard
1: The variable called keyboard is updated
2: We work out where in the game the player is standing
3: The player is set to move if an arrow key is pressed
4: We check what type of tile the player would move to
5: If the player would end up on some floor (i.e. not in the wall), then they do move
'''
def on_key_down(key):
    global keyboard
    if key in keyboard_variables:
        keyboard = keyboard_variables.get(key)
        #print(keyboard)
    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if keyboard == 'up':
        row = row - 1
    if keyboard == 'down':
        row = row + 1
    if keyboard == 'left':
        column = column - 1
    if keyboard == 'right':
        column = column + 1

    tile = shop_tiles[shop_map[row][column]]
    #print(tile)

    if tile == 'floor':
        player.x = column * TILE_SIZE
        player.y = row * TILE_SIZE


'''
Game loop for the shop
Set a question variable, to keep track of how far along in the conversation you are
If the player presses the escape key, reset the dialog
Update the dialog and allow the player to answer questions
When you get to question = 2, the player chooses an item to buy
The chosen item is put into player_items and removed from shopkeeper_items
'''
question = 0
def shop_dialog():
    global shop_text, keyboard, question

    if keyboard == 'escape':
        shop_text = 'Hello, welcome to my shop! \nCome to the till and press SPACE'
        question = 0

    if question == 0:
        if keyboard == 'i':
            inventory = "You own: "
            for item in player_items:
                inventory += item + "   "
            shop_text = inventory

        elif keyboard == 's':
            stats = "You have: "
            for key, value in player_stats.items():
                stats += str(key) + ": " + str(value) + "   "
            shop_text = stats

        elif till.colliderect(player) and keyboard == 'space':
            shop_text = "I have " + str(len(shopkeeper_items)) + " types of tea for sale today, they each cost \xA35" + "\n" + "Type Y or N"
            question = 1

    if question == 1:
        if keyboard == 'y':
            shop_items = ""
            for item in shopkeeper_items:
                shop_items += str(shopkeeper_items.index(item)) + ' = ' + item + "   "
            shop_text = shop_items + "\n" + "Type the number of the item you want to buy"
            question = 2
        elif keyboard == 'n':
            shop_text = "Goodbye!"
            question = 0

    if question == 2:
        if keyboard == 'n':
            shop_text = "Goodbye!"
            question = 0
        elif isinstance(keyboard, int):
            if 0 <= keyboard < len((shopkeeper_items)):
                if player_stats['money'] >= 5:
                    bought_thing = shopkeeper_items[keyboard]
                    shop_text = "Okay! You now own " + bought_thing + "."
                    player_items.append(bought_thing)
                    shopkeeper_items.pop(keyboard)
                    #player_items.append(shopkeeper_items.pop(keyboard))
                    player_stats['money'] -= 5
                    shopkeeper_stats['money'] += 5
                    question = 0
                else:
                    shop_text = "You can't afford that! Goodbye."
                    question = 0
            else:
                shop_text = "I don't sell that! Goodbye."
                question = 0

    return



'''
Run the game loop every 0.03 seconds
draw() and on_key_down() are run automatically by PyGameZero, so we don't need to call these functions seperately
'''
clock.schedule_interval(shop_dialog, 0.03)
