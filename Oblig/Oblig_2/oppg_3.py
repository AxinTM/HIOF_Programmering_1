# Lister med filmer fra Tolkien.
tolkien_list = ["The Hobbit", "Farmer Giles of Ham",
                "The Fellowship of the Ring",
                "The Two Towers",
                "The Return of the King",
                "The Adventures of Tom Bombadil",
                "Tree and Leaf"]
# Printer ut de 2 første og 2 siste filmene fra listen.
print(f"======First 2 and last 2 books from list:======"
      f"\n{tolkien_list[0]}, {tolkien_list[1]}, {tolkien_list[5]},{tolkien_list[-1]}.")
# Legger til to nye filmer på slutten av listen.
tolkien_list.append("The Silmarillion")
tolkien_list.append("Unfinished Tales")

print(f"\n======Added two more books after Tolkien death====== \n{tolkien_list}.")
# Legge til Lord of the Ring i 3 av filmene til Tolkien.
tolkien_list[2] = "Lord of the Rings: The Fellowship of the Ring"
tolkien_list[3] = "Lord of the Ring: The Two Towers"
tolkien_list[4] = "Lord of the Ring: The Return of the King"

# lotr = "Lord of the Ring:"
# for index in range(2,5):
#   tolkien_list[index] = lotr + tolkien_list[index]

# Sortere filmene i alfabetisk rekkefølge.
tolkien_list.sort()

print(f"\n======List in Ascending order====== \n{tolkien_list}")
