# Her importerers randrange fra et bibliotek som heter random
from random import randrange

close = False
sets = 1
# når parameter close er False så kjører koden.
while not close:
    user = input("\nHow many player? ")
    try:
        user = int(user)
    # Om det ikke er tall, gi beskjed om å skrive et tall.
    except ValueError:
        number = None
        print("\nYou have to enter a integer.")
        # Dersom ValueError dukker opp, koden stoppes.
        exit("Rerun the program!")
    point = []
    rounds = 1
    player = rounds
# kjører en for loop for antal user som er valgt
    for player in range(user):
        print(f"\n=======Player {player+1}, Round {sets}=======")
        # kjører 3 ganger, da de skal kaste 3 dart piler
        for tries in range(3):
            throw = randrange(0, 61)
            print(f"{throw} point!")
            point.append(throw)
        print(f"===Player {player+1}, got {sum(point)} point!===")
        rounds += 1
        point.clear()

# spør brukeren om de ønsker å spille igjen, om nei, avslutt spillet
    play_again = input("\nDo you want to play again? ( Y/N) ")
    if play_again.upper() == "Y":
        sets += 1
        close = False
    else:
        close = True
