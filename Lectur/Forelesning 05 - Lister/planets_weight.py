print("==================================================")
print("=====What is your weight on another planets?======")
print("==================================================")

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune']
planets_gravity = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

print("\n====Plantets====")
print(f"1 - {planets[0]}")
print(f"2 - {planets[1]}")
print(f"3 - {planets[2]}")
print(f"4 - {planets[3]}")
print(f"5 - {planets[4]}")
print(f"6 - {planets[5]}")
print(f"7 - {planets[6]}")
print(f"8 - {planets[7]}")
print("=================")

planets_number = input("\nPick a planet by typing a number: ")
planets_number = int(planets_number)-1

chosen_planets = planets[planets_number]
print(f"\nYou Picked: {planets[planets_number]}")

your_weight = int(input("\nType in your weight in kg on earth: "))

earth_gravity = planets_gravity[2]
your_mass = your_weight / planets_gravity[2]
your_weight_on_another_planet = your_mass * planets_gravity[planets_number]

print(f"You will weight {round(your_weight_on_another_planet, 2)}kg on the planet {chosen_planets}")
