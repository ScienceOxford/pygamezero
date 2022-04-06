"""
Set up the game"s size - this is based on the size of the tiles you are using
Each "tile" is 64x64 pixels
"""
TILE_SIZE = 64
WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 12



"""
Set up the shop background
shop_tiles is a list of all the images that make up the background
shop_map is a list of where each image should go in an x,y grid
"""
shop_tiles = ["floor",
              "bench_corner",
              "bench_bottom",
              "bench_side",
              "wall",
              "textbox"]
shop_map = [ [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 2, 2, 2, 1, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 4, 4, 4, 4, 4, 4, 0, 4, 4],
             [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
             [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
             ]



"""
Set up the orchard background
orchard_tiles is a list of all the images that make up the background
orchard_map is a list of where each image should go in an x,y grid
"""
orchard_tiles = ["grass1",
                 "grass2",
                 "outside_wall",
                 "textbox"]
orchard_map = [ [2, 2, 2, 2, 2, 2, 2, 0, 2, 2],
                [2, 0, 1, 0, 1, 0, 0, 1, 0, 2],
                [2, 0, 1, 0, 0, 0, 1, 0, 0, 2],
                [2, 0, 0, 0, 1, 0, 1, 0, 1, 2],
                [2, 0, 0, 1, 1, 0, 1, 0, 1, 2],
                [2, 0, 0, 1, 0, 1, 0, 0, 0, 2],
                [2, 0, 1, 0, 1, 0, 0, 1, 0, 2],
                [2, 0, 1, 0, 0, 1, 0, 0, 0, 2],
                [2, 1, 1, 0, 0, 1, 1, 0, 0, 2],
                [2, 0, 2, 2, 2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
             ]



"""
Set up the characters
player and shopkeeper have an image and a start position
player and shopkeeper have a list of the items they are carrying
till does not have any items, but it is a character so that the player can interact with it
"""
player = Actor("player", anchor=(0, 0), pos=(7 * TILE_SIZE, 8 * TILE_SIZE))
player_items = ["paper", "pen", "phone", "money"]

shopkeeper = Actor("shopkeeper", anchor=(0,0), pos=(2 * TILE_SIZE, 3 * TILE_SIZE))
shopkeeper_items = ["tea", "coffee", "water", "orange juice"]

till = Actor("till", anchor=(0,0), pos=(2 * TILE_SIZE, 4.5 * TILE_SIZE))

tree1 = Actor("foliage_006", anchor=(0,0), pos=(1 * TILE_SIZE, 1 * TILE_SIZE))
tree1_items = ["apple", "apple", "apple", "apple"]
tree2 = Actor("foliage_008", anchor=(0,0), pos=(3 * TILE_SIZE, 5.5 * TILE_SIZE))
tree2_items = ["pear", "pear", "pear", "pear"]
tree3 = Actor("foliage_010", anchor=(0,0), pos=(5.75 * TILE_SIZE, 4.5 * TILE_SIZE))
tree3_items = ["cherry", "cherry", "cherry", "cherry"]



"""
Set what text should be shown at the start, then draw everything onto the screen
1: draw the background, using the tile information given above
2: draw the till, the player, then the shopkeeper in their positions
3: draw the text in the text box, at a set position
"""
text_box = "Hello, welcome to my shop!" + "\n" + "Come to the till and press SPACE"
def draw():
    global text_box

    screen.clear()

    if location == "shop":
        for row in range(len(shop_map)):
            for column in range(len(shop_map[row])):
                x = column * TILE_SIZE
                y = row * TILE_SIZE
                tile = shop_tiles[shop_map[row][column]]
                screen.blit(tile, (x, y))
        till.draw()
        shopkeeper.draw()

    elif location == "orchard":
        for row in range(len(orchard_map)):
            for column in range(len(orchard_map[row])):
                x = column * TILE_SIZE
                y = row * TILE_SIZE
                tile = orchard_tiles[orchard_map[row][column]]
                screen.blit(tile, (x, y))
        tree1.draw()
        tree2.draw()
        tree3.draw()

    player.draw()
    screen.draw.text(text_box, (0.5 * TILE_SIZE, 10.5 * TILE_SIZE), color="black")



"""
Set up which keyboard buttons can be used by the game
keyboard_variables is a dictionary pairing the key presses with a value - this is useful for keeping track of what you press during the game
keyboard will be set to the last key pressed - it is set to False at the start of the game
"""
keyboard_variables = {keys.UP: "up", keys.DOWN: "down", keys.LEFT: "left", keys.RIGHT: "right", keys.SPACE: "space", keys.ESCAPE: "escape", keys.RETURN: "return",
                    keys.Y: "y", keys.N: "n", keys.I: "i", keys.S: "s",
                    keys.KP0: 0, keys.KP1: 1, keys.KP2: 2, keys.KP3: 3, keys.KP4: 4, keys.KP5: 5, keys.KP6: 6, keys.KP7: 7, keys.KP8: 8, keys.KP9: 9,
                    keys.K_0: 0, keys.K_1: 1, keys.K_2: 2, keys.K_3: 3, keys.K_4: 4, keys.K_5: 5, keys.K_6: 6, keys.K_7: 7, keys.K_8: 8, keys.K_9: 9}
keyboard = False



"""
Define what happens when you press a key on the keyboard
1: The variable called keyboard is updated
2: We work out where in the game the player is standing
3: The player is set to move if an arrow key is pressed
4: We check what type of tile the player would move to
5: If the player would end up on some floor (i.e. not in the wall), then they do move
"""
def on_key_down(key):
    global keyboard

    if key in keyboard_variables:
        keyboard = keyboard_variables.get(key)
        #print(keyboard)

    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if keyboard == "up":
        row = row - 1
    elif keyboard == "down":
        row = row + 1
    elif keyboard == "left":
        column = column - 1
    elif keyboard == "right":
        column = column + 1

    if location == "shop":
        tile = shop_tiles[shop_map[row][column]]
    elif location == "orchard":
        tile = orchard_tiles[orchard_map[row][column]]
    #print(tile)

    if tile == "floor" or tile == "grass1" or tile == "grass2":
        player.x = column * TILE_SIZE
        player.y = row * TILE_SIZE

"""
Game loop for the shop
If the player presses the escape key, reset the dialog
Update the dialog and allow the player to answer questions
"""
def shop():
    global text_box, keyboard, progress, location

    if keyboard == "escape":
        text_box = "Hello, welcome to my shop!" + "\n" + "Come to the till and press SPACE"
        progress = 0

    if progress == 0:
        if keyboard == "i":
            inventory = "You own: "
            for item in player_items:
                inventory += item + "   "
            text_box = inventory

        elif till.colliderect(player) and keyboard == "space":
            text_box = "Would you like to buy something?" + "\n" + "Type Y or N"
            progress = 1

        elif player.pos == (7 * TILE_SIZE, 9 * TILE_SIZE) and keyboard == "space":
            text_box = "You are at the door. Would you like to leave?" + "\n" + "Type Y or N"
            progress = 199

    elif progress == 1:
        if keyboard == "y":
            shop_items = ""
            for item in shopkeeper_items:
               shop_items += str(shopkeeper_items.index(item)) + " = " + item + "   "
            text_box = shop_items + "\n" + "Type the number of the item you want to buy"
            progress = 2

        elif keyboard == "n":
            text_box = "Goodbye!" + "\n" + "Press ESCAPE to end the conversation."
            progress = 0

    elif progress == 2:
        if isinstance(keyboard, int):
            if 0 <= keyboard < len((shopkeeper_items)):
                bought_thing = shopkeeper_items[keyboard]
                text_box = "Okay! You now own " + bought_thing + "." + "Press ESCAPE to end the conversation."
                player_items.append(bought_thing)
                shopkeeper_items.remove(bought_thing)
                progress = 0

            else:
                text_box = "I don't sell that! Goodbye." + "Press ESCAPE to end the conversation."
                progress = 0

        elif keyboard == "n":
            text_box = "Goodbye!" + "\n" + "Press ESCAPE to end the conversation."
            progress = 0

    elif progress == 199:
        if keyboard == "y":
            text_box = "You are in the orchard." + "\n" + "To harvest, walk up to a tree and press SPACE"
            player.pos = (7 * TILE_SIZE, 1 * TILE_SIZE)
            progress = 20
            location = "orchard"

        elif keyboard == "n":
            text_box = "Hello, welcome to my shop!" + "\n" + "Come to the till and press SPACE"
            progress = 0
    return

"""
Game loop for outside
If the player presses the escape key, reset the dialog
Update the dialog and allow the player to answer questions
"""
def orchard():
    global text_box, keyboard, progress, location

    if keyboard == "escape":
        #print(location)
        text_box = "You are in the orchard." + "\n" + "To harvest, walk up to a tree and press SPACE"
        progress = 20

    if progress == 20:
        if keyboard == "i":
            inventory = "You own: "
            for item in player_items:
                inventory += item + "   "
            text_box = inventory

        elif player.pos == (7 * TILE_SIZE, 0 * TILE_SIZE) and keyboard == "space":
            text_box = "You are at the door. Would you like to enter the shop?" + "\n" + "Type Y or N"
            progress = 299


        elif tree1.colliderect(player) and keyboard == "space":
            text_box = "This is an apple tree!" + "\n" + "Press ESCAPE to keep harvesting"
            if len(tree1_items) > 0:
                player_items.append("apple")
                tree1_items.pop(0)
            else:
                text_box = "This is an empty apple tree!" + "\n" + "Press ESCAPE to try another tree"
            progress = 21
        elif tree2.colliderect(player) and keyboard == "space":
            if len(tree2_items) > 0:
                text_box = "This is a pear tree!" + "\n" + "Press ESCAPE to keep harvesting"
                player_items.append("pear")
                tree2_items.pop(0)
            else:
                text_box = "This is an empty pear tree!" + "\n" + "Press ESCAPE to try another tree"
            progress = 21
        elif tree3.colliderect(player) and keyboard == "space":
            if len(tree3_items) > 0:
                text_box = "This is a cherry tree!" + "\n" + "Press ESCAPE to keep harvesting"
                player_items.append("cherry")
                tree3_items.pop(0)
            else:
                text_box = "This is an empty cherry tree!" + "\n" + "Press ESCAPE to try another tree"
            progress = 21

    elif progress == 21:
        if keyboard == "escape":
            text_box = "You are in the orchard." + "\n" + "To harvest, walk up to a tree and press SPACE"
            progress = 20

    elif progress == 299:
        if keyboard == "y":
            text_box = "Hello, welcome to my shop!" + "\n" + "Come to the till and press SPACE"
            player.pos = (7 * TILE_SIZE, 8 * TILE_SIZE)
            progress = 0
            location = "shop"
        elif keyboard == "n":
            text_box = "You are in the orchard." + "\n" + "To harvest, walk up to a tree and press SPACE"
            progress = 20
    return



"""
Set the starting location and dialog start point
Set the main game loop - this runs the dialog for the location you are in
"""
location = "shop"
progress = 0
def update():
    if location == "shop":
        shop()
    elif location == "orchard":
        orchard()

"""
draw(), on_key_down(), and update() are run automatically by PyGameZero
We don't need to call these functions seperately like you would in 'regular' Python
They run while the game is running
"""
