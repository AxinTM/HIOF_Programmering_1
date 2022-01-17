lotr_triologi = []

tolkien_list = ["Farmer Giles of Ham"
                "The Hobbit", "Farmer Giles of Ham",
                "The Fellowship of the Ring",
                "The Two Towers",
                "The Return of the King",
                "The Adventures of Tom Bombadil",
                "Tree and Leaf"]

print("\n=============1st=============")
for lotr in lotr_triologi:
    print(f"{lotr}")

print("\n=============2nd=============")
for lotr in range(len(lotr_triologi)):
    print(f"{lotr_triologi[lotr]}")

print("\n=============3rd=============")
x = 0
for lotr in range(len(lotr_triologi)):
    print(lotr_triologi[x])
    x += 1
