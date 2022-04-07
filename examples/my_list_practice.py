
player_items = ['paper', 5, 'hello', '5']

print(player_items)
print(player_items[0])
print(player_items[-1])

player_items[0] = 'pen'
print(player_items)
print(player_items[0])



player_items = ['paper', 'pen', 'money', 'phone']
shopkeeper_items = ['tea', 'coffee', 'water', 'orange juice']

print(player_items)
print(shopkeeper_items)

bought_thing = shopkeeper_items[0]
print('You bought ' + bought_thing)

player_items.append(bought_thing)
shopkeeper_items.remove(bought_thing)
player_items.insert(0, bought_thing)
shopkeeper_items.pop(0)
print(player_items)
print(shopkeeper_items)
