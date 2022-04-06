# Set up the game's size - this is based on the size of the tiles you are using
TILE_SIZE = 64
WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 10

# Room 1 data - the shop
# location = 'Shop'
shop_tiles = ['floor',
              'bench_corner',
              'bench_bottom',
              'bench_side',
              'wall']
shop_map = [ [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 3, 0, 0, 0, 0, 4],
             [4, 2, 2, 2, 1, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [4, 4, 4, 4, 4, 4, 4, 0, 0, 4] ]

player = Actor('player', anchor=(0, 0), pos=(7 * TILE_SIZE, 8 * TILE_SIZE))
player_items = []

shopkeeper = Actor('shopkeeper', anchor=(0,0), pos=(2 * TILE_SIZE, 3 * TILE_SIZE))
shopkeeper_items = ['oolong', 'green', 'white', 'black', 'puerh']

till = Actor('till', anchor=(0,0), pos=(2 * TILE_SIZE, 4.5 * TILE_SIZE))

def draw():
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


def on_key_down(key):
    row = int(player.y / TILE_SIZE)
    column = int(player.x / TILE_SIZE)
    if key == keys.UP:
        row = row - 1
    if key == keys.DOWN:
        row = row + 1
    if key == keys.LEFT:
        column = column - 1
    if key == keys.RIGHT:
        column = column + 1
    if key == keys.SPACE:
        print('You own the following items:')
        print(player_items)
        print()

    tile = shop_tiles[shop_map[row][column]]
    #print(tile)

    if till.colliderect(player) and key == keys.SPACE:
        shop_dialog()

    if tile == 'floor':
        player.x = column * TILE_SIZE
        player.y = row * TILE_SIZE


def shop_dialog():
    print()
    print('Hello, welcome to my shop!')
    print('Would you like to buy something today?')

    q1 = input('Type Y to see shop items, type N to return: ')
    if q1 == 'Y':
        print()
        print('I have ' + str(len(shopkeeper_items)) + ' types of tea for sale today!')
        print('Which would you like to buy?')
        for item in shopkeeper_items:
            print(str(shopkeeper_items.index(item)) + ' = ' + item)

        q2 = input('Type which number you would like to buy: ')
        print()

        try:
            bought_index = int(q2)
        except:
            print("Sorry, I don't sell that item!")

        if 0 <= bought_index < len((shopkeeper_items)):
            bought_thing = shopkeeper_items[bought_index]
            print('Okay! You now own ' + bought_thing + ' tea.')
            print()
            player_items.append(bought_thing)
            shopkeeper_items.pop(bought_index)
            #player_items.append(shopkeeper_items.pop(bought_index))
            return

        else:
            print("Sorry, I don't sell that item!")
            return

    print('Goodbye!')
    print()
    return
