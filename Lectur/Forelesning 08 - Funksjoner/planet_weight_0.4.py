import random

planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
planets_gravity = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

close = False
while not close:
    print("\n=========================================================")
    print("==========What is your weight on other planets?==========")
    print("=========================================================")
    print("0 - Random Planet")
    for planet_number in range(len(planets)):
        print(f"{planet_number+1} - {planets[planet_number]}")

    planet_number = input("\nPick a planet by typing a number: ")
    # Må gjøre nummret til et tall, og rette opp tallet til å peke på riktig index (vi starter jo på 0)
    planet_number = int(planet_number)-1

    # If input is 0 - pick random planet
    if planet_number == -1:
        planet_number = random.randrange(0, 8)
        chosen_planet = planets[planet_number]
        print(f"\nYou got: {chosen_planet}")
    else:
        chosen_planet = planets[planet_number]
        print(f"\nYou picked planet: {chosen_planet}")

    your_weight = float(input("\nType in your weight in kg on earth: "))

    earth_gravity = planets_gravity[2]
    your_weight_on_other_planet = your_weight / earth_gravity * planets_gravity[planet_number]

    print(f"\nYou will weigh {round(your_weight_on_other_planet, 2)}kg on the planet {chosen_planet}")

    answer = input("\nDo you want to try again (Y/N)?")
    if answer.upper() != 'Y':
        close = True
