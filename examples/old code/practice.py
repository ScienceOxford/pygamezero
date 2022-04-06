# Set up the game's size - this is based on the size of the tiles you are using
TILE_SIZE = 64
WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 10
room_width = WIDTH//TILE_SIZE
room_height = HEIGHT//TILE_SIZE
# Today, every room will be the same size, to simplify the code

# Room 1 data - the shop
# location = 'Shop'
shop_tiles = [images.floor,
              images.bench_corner,
              images.bench_bottom,
              images.bench_side,
              images.wall,
              images.shopkeeper]
shop_map = [ [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 0, 5, 0, 3, 0, 0, 0, 0, 4],
             [4, 2, 2, 2, 1, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 4, 4, 4, 4, 4, 4, 0, 0, 4]
           ]

# Room 2 data - the path
# location = 'Path'
path_tiles = []
path_map = []

# Room 3 data - the house
# location = 'House'
house_tiles = []
house_map = []

# Player character set up instructions
player_x = 7*TILE_SIZE
player_y = 8*TILE_SIZE
player_speed = 5
player_location = "Shop"
player = Actor('player', anchor=('left', 'top'))
player.pos = player_x, player_y

# What to draw on the screen
def draw():
    if player_location == "Shop":
        for y in range(room_width):
            for x in range (room_height):
                image_to_draw = shop_tiles[shop_map[y][x]]
                screen.blit(image_to_draw, (x*TILE_SIZE, y*TILE_SIZE))
    elif player_location == "Path":
        pass
    elif player_location == "House":
        pass
    #screen.blit(images.player, (player_x, player_y))
    player.draw()

def game_loop():
    global player_x, player_y
    player_y_tile = int(player_y//TILE_SIZE)
    player_x_tile = int(player_x//TILE_SIZE)
    print(shop_map[player_y_tile][player_x_tile])
    '''
    #old_player_pos = (player.x, player.y)
    old_player_y = player_y
    old_player_x = player_x
    #print(player.y, old_player_y)
    #print(player.x, old_player_x)
    print(player_y_tile, player_x_tile)
    print(shop_map[player_y_tile][player_x_tile])
    #print(player.y, player.x)
    if shop_map[player_y_tile][player_x_tile] == 0:
        if keyboard.left:
            player_x -= 1
        if keyboard.right:
            player_x += 1
        if keyboard.up:
            player_y -= 1
        if keyboard.down:
            player_y += 1
    else:
        player_y = old_player_y
        player_x = old_player_x
        '''
    if keyboard.left:
        player_x -= 5
        if shop_map[player_y_tile][player_x_tile] != 0:
            animate(player, pos=(player_speed+1, player_y), duration=0.001)
    if keyboard.right:
            player_x += 5

clock.schedule_interval(game_loop, 0.03)
