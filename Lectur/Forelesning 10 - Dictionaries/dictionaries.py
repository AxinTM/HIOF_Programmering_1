board_game = {
    'titel': 'Dixit',
    'playtime': '30',
    'age': 8}

# print(board_game) - Get the hole dictionaries
# print(board_game[0]) - Can't use this, because there are no index [0],[1], etc.....
print(board_game['titel'])
print(f"{board_game.get('playtime')} min")
