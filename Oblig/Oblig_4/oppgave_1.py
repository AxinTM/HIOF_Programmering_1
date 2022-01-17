import random

# Her har jeg laget en funksjon for at brukeren skal kunne velge hvor mye de ønsker å satse,
# og jeg har også satt inn en try-except for å ta vekk ValueError som kan oppstå.


def players_bet():
    global player_chips
    try:
        bet = int(input(f'\nYou have {player_chips} chips, how many chips do you want to bet? '))
        if bet > player_chips:
            print("You can't bet more than you got!!")
            players_bet()
        elif bet < 1:
            print("You can't bet less then 1 chips!!")
            players_bet()
        else:
            print(f"You bet {bet} chips:")
            return bet
    except ValueError:
        print('\nYou have to enter the amount of chips you want to bet, please try again!')
        players_bet()


def shuffled_deck():
    deck_shuffled = list(full_deck.keys())
    random.shuffle(deck_shuffled)
    return deck_shuffled


def player_draw():
    player_card.append(deck.pop(0))


def dealer_draw():
    dealer_card.append(deck.pop(0))


# Her kunne jeg nok ha laget en funksjon slik at begge def get_player_point og get_dealer_point hadde vært en funksjon
# og heller satt inn parameter for å hente informasjonen vi skulle ha brukt.


def get_player_point():
    total = 0
    for card in player_card:
        total += full_deck[card]
    if total > 21 and any("Ace" in s for s in player_card):
        total -= 10
    return total


def get_dealer_point():
    total = 0
    for card in dealer_card:
        total += full_deck[card]
    if total > 21 and any("Ace" in s for s in player_card):
        total -= 10
    return total


def hit_or_stand():
    global player_chips
    global player_bet
    user_choice = input(f'\nYou got {get_player_point()}, do you want to Hit(H) or Stand(S)? (H/S) ')
    if user_choice.upper() == 'H':
        player_draw()
        print(f'Your new card is {player_card[len(player_card)-1]}, and your new total is: {get_player_point()}.')
        if get_player_point() > 21:
            print(f'\nYou Busted, your total point is {get_player_point()}.')
            player_chips -= player_bet
            print(f'\nYour total chips is {player_chips}.')
            play_again()
    elif user_choice.upper() == 'S':
        print(f'\nDealers card is {dealer_card[0]} and {dealer_card[1]}.')
        run = True
        while run:
            if get_dealer_point() >= 17:
                break
            dealer_draw()
            print(f'\nDealer drew {dealer_card[len(dealer_card) - 1]}.')
        print(f'\nYour total point is {get_player_point()} and dealers point is {get_dealer_point()}.')
        win_or_lose()


def win_or_lose():
    global player_chips
    global player_bet
    if get_dealer_point() > 21:
        print('Dealer busted, you WON!')
        player_chips += player_bet
        print(f'\nYour total chips is {player_chips}.')
        play_again()
    elif get_player_point() > get_dealer_point():
        print('You have higher point then dealer, you WON')
        player_chips += player_bet
        print(f'\nYour total chips is {player_chips}.')
        play_again()
    elif get_player_point() < get_dealer_point():
        print('Dealers point is higher than your, Dealer WON')
        player_chips -= player_bet
        print(f'\nYour total chips is {player_chips}.')
        play_again()
    elif get_player_point() == get_dealer_point():
        print('Dealer and your point is the same, neither lose or win.')
        print('Your chips stay the same.')
        print(f'\nYour total chips is {player_chips}.')
        play_again()


def play_again():
    zero_chips()
    restart_game = input('\nDo you want to play again? (Y/N)')
    if restart_game.upper() == 'Y':
        dealer_card.clear()
        player_card.clear()
        start_game()
    elif restart_game.upper() == 'N':
        exit('Welcome Back')
    else:
        play_again()


def start_game():
    print('\n=====Welcome to BlackJack=====')
    global deck, player_chips, player_bet
    deck = shuffled_deck()
    player_bet = players_bet()
    player_draw()
    dealer_draw()
    player_draw()
    dealer_draw()

    player_total = get_player_point()
    print(f'\nPlayer have {player_card[0]} and {player_card[1]}, and you total point is {player_total}.')
    print(f'Dealers visible card is {dealer_card[0]}.')

    if get_player_point() == 21:
        print('\n======You got BlackJack, CONGRATULATION YOU WON!!!======')
        player_chips += player_bet * 2
        print(f'\nYour total chips is {player_chips}')
        play_again()


def zero_chips():
    if player_chips <= 0:
        exit('You need to refill you chips!')


full_deck = {
    "Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5, "Six of clubs": 6,
    "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
    "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,
    "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5,
    "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9,
    "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10,
    "Ace of diamonds": 11,
    "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6,
    "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
    "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,
    "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
    "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
    "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
       }

player_chips = int(5)
player_bet = int(0)
player_card = []
dealer_card = []
deck = shuffled_deck()


start_game()

game = True
while game:
    hit_or_stand()
