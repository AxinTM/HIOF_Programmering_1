import random

planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
planets_gravity = 3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15

close = False


def user_picked_planet(planets, planet_number):
    if planet_number == -1:
        planet_number = random.randrange(0, 8)
        chosen_planet = planets[planet_number]
        print(f"\nYou got: {chosen_planet}")
    else:
        chosen_planet = planets[planet_number]
        print(f"\nYou picked: {chosen_planet}")
    return chosen_planet


def calculate_weight_on_planet(your_weight, planet_gravity):
    earth_gravity = 9.807
    # your_weight / earth_gravity * other_planet_gravity
    calculated_weight = your_weight / earth_gravity * planets_gravity
    return calculated_weight


while not close:
    print("\n==============================================")
    print("====What is your weight on another planet?====")
    print("==============================================")
    print("0 - Random Planet")
    for planet_number in range(len(planets)):
        print(f"{planet_number + 1} - {planets[planet_number]}")

    planet_number = input("\nPick a planet by typing a number: ")
    planet_number = int(planet_number) - 1

    # If input is 0 - pick random planet
    chosen_planet = user_picked_planet(planets, planet_number)

    your_weight = float(input("\nType in your weight in kg on earth: "))

    your_weight_on_other_planet = calculate_weight_on_planet(your_weight, planets_gravity[planet_number])

    print(f"\nYou will weigh {round(your_weight_on_other_planet, 2)}kg on the planet {chosen_planet}")

    answer = input("\nDo you want to try again(Y/N)?  ")
    close = answer.upper() != 'Y'
