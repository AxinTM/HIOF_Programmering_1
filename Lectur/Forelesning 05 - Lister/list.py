random_list = ["Europe", "Dog", 42, 9001.34, "Apex", ["Another List", 2]]
print(random_list)

planets = ['Mercury', 'Venus', 'Earth', 'Jupiter', 'Saturne', 'Uranus']

print(planets)
print(planets[0])
print(planets[0].upper())
earth = planets[2]
print(earth)

planets[4] = "Saturne"
print(f"\nAfter correction: {planets}")

planets.append('Neptune')
planets.append('Pluto')
planets.append('Eris')
planets.append('Makemake')
print(f"\nAfter append: {planets}")

planets.insert(3, 'Mars')
planets.insert(3, 'Mars')
planets.insert(3, 'Tellus')
print(f"\nAfter insert: {planets}")

planets.pop()
print(f"\nAfter pop: {planets}")
print(planets.pop())
print(f"\nAfter pop: {planets}")

planets.pop(3)
print(f"\nAfter pop: {planets}")

planets.remove('Mars')
print(f"\nAfter remove: {planets}")
pluto = 'Pluto'
print(planets.remove('Pluto'))
print(f"\nAfter remove: {planets}")

print(f"\nTemp sorted list: {sorted(planets)}")
print(f"Original list : {planets}")

planets_sorted = sorted(planets) # Make a sorted copy of the list

planets.reverse()
print(f"Reversed list : {planets}")

planets.sort()
print(f"\nSorted list: {planets}")

planets.sort(reverse=True)
print(f"\nSorted desc. list: {sorted(planets)}")

number_of_planets = len(planets)
print(f"\nThe number of planets in our solar system is {number_of_planets}")

print(f"The last planet in our solar system: {planets[-1]}")

planets.clear()
print(f"\nOur planets after the sun explodes: {planets}")
