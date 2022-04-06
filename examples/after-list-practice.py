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
Set up the characters
player and shopkeeper have an image and a start position
player and shopkeeper have a list of the items they are carrying
till does not have any items, but it is a character so that the player can interact with it
"""
player = Actor("player", anchor=(0, 0), pos=(7 * TILE_SIZE, 8 * TILE_SIZE))
player_items = []

shopkeeper = Actor("shopkeeper", anchor=(0,0), pos=(2 * TILE_SIZE, 3 * TILE_SIZE))
shopkeeper_items = []

till = Actor("till", anchor=(0,0), pos=(2 * TILE_SIZE, 4.5 * TILE_SIZE))



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

    if tile == "floor":
        player.x = column * TILE_SIZE
        player.y = row * TILE_SIZE



"""
Game loop for the shop
Set a question variable, to keep track of how far along in the conversation you are
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
            print(player_items)
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
                text_box = "Okay! You now own " + bought_thing + "." + "\n" + "Press ESCAPE to end the conversation."
                print(player_items)
                progress = 0

            else:
                text_box = "I don't sell that! Goodbye." + "\n" + "Press ESCAPE to end the conversation."
                progress = 0

        elif keyboard == "n":
            text_box = "Goodbye!" + "\n" + "Press ESCAPE to end the conversation."
            progress = 0

    elif progress == 199:
        if keyboard == "y":
            text_box = "Sorry, the door is locked." + "\n" + "Press ESCAPE to continue."
            progress = 0
        elif keyboard == "n":
            text_box = "Okay!" + "\n" + "Press ESCAPE to end the conversation."
            progress = 0

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

"""
draw(), on_key_down(), and update() are run automatically by PyGameZero
We don't need to call these functions seperately like you would in 'regular' Python
They run while the game is running
"""
