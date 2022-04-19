"""
Set up the game's size - this is based on the size of the tiles you are using
"""
TILE_SIZE = 64
WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 12



"""
Set up the outside background
outside_tiles is a list of all the images that make up the background
outside_map is a list of where each image should go in an x,y grid
"""
outside_tiles = ["floor2",
                 "wall2",
                 "textbox"]
outside_map = [ [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
                ]



"""
Set up the characters
"""
player = Actor("player", anchor=(0, 0), pos=(7 * TILE_SIZE, 8 * TILE_SIZE))



"""
Set what text should be shown at the start, then draw everything onto the screen
"""
text_box = "You are outside!"
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

    elif location == "outside":
        for row in range(len(outside_map)):
            for column in range(len(outside_map[row])):
                x = column * TILE_SIZE
                y = row * TILE_SIZE
                tile = outside_tiles[outside_map[row][column]]
                screen.blit(tile, (x, y))

    player.draw()
    screen.draw.text(text_box, (0.5 * TILE_SIZE, 10.5 * TILE_SIZE), color="black")



"""
Game loop for outside
"""
def outside():
    pass



"""
Set the starting location and dialog start point
Set the main game loop - this runs the dialog for the location you are in
"""
location = "outside"
progress = 0
def update():
    if location == "shop":
        shop()
    elif location == "outside":
        outside()
