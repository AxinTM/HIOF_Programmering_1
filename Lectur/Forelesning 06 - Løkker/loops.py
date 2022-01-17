board_games = ['Ubongo', 'Pademic', 'Ticket To Ride', 'Monopoly', 'Mysterium']

for board_game in board_games:
    print(f"{board_game} is a good game!")
    print("You should try it!\n")

for character in 'Risk':
    print(character)

print("")

#for value in range(1, 11):
   # print(value)

pandemic_legacy_season = 'Pandemic Legacy: Season 1'

if pandemic_legacy_season not in board_games:
    print(f"{pandemic_legacy_season} is not in the collection. That's a shame. Let's add it!")
    board_games.append(pandemic_legacy_season)

print("\nBoard game out collection:")
for board_game in board_games:
    print(board_game)

