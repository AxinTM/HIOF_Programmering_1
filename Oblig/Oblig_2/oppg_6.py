luggage = []
options = ["Shoes", "Underwear", "Trouser", "Socks", "Jacket", "Sweaters", "Hats", "BDSM"]

close = False
done = False
# definere print_list som en funksjon
def print_list(x):
    number = 0
    for item in x:
        print(f"{number +1}. {x[number]}")
        number += 1
while not close:
    print("\n====What do you want to pack for your next trip====")
    print_list(options)
    selected_item = input("\nSelect the number that you want to add: ")
    try:
        selected_item = int(selected_item)
    except ValueError:
        selected_item = None
        print("You have to enter a integer.")
        exit("Rerun the program!")
    # legger til et produkt i listen luggage.
    selected_item = int(selected_item)
    luggage.append(options[selected_item - 1])
    print(luggage)

# spørr om vi ønsker å legge flere produkter
    add_more_item = input("\nDo you want to add more item? ( Y/N) ")
    if add_more_item.upper() == "Y":
        close = False
    elif add_more_item.upper() == "N":
        close = True
        print_list(luggage)
        # gir en melding da brukeren ikke svarer "Y/N"
    else:
        exit(f'''Next time type in "Y" or "N"!''')

are_you_done = input("\nDo you want to remove something from the list? (Y/N) ")
if are_you_done.upper() == "Y":
    done = False
elif are_you_done.upper() == "N":
    done = True
    print_list(luggage)
else:
    exit(f'''Next time type in "Y" or "N"!''')


while not done:
    print("\n====What do you want to remove? ====")
    print_list(luggage)
    selected_item = input("\nSelect the number that you want to remove: ")
    try:
        selected_item = int(selected_item)
    except ValueError:
        selected_item = None
        print("You have to enter a integer.")
        exit("Rerun the program!")
    selected_item = int(selected_item)
    luggage.pop(selected_item - 1)
    print(luggage)
    remove_item = input("Are you done removing items? (Y/N) ")
    if remove_item.upper() == "Y":
        done = True
    elif remove_item.upper() == "N":
        done = False
        print_list(luggage)
    else:
        exit(f'''Next time type in "Y" or "N"!''')
print("\nThis is your packed list!!")
print_list(luggage)
print("\nHave a nice trip")
