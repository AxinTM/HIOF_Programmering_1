def rectangle(length, wide):
    perimeter = 2 * (length + wide)
    return perimeter


close = False
while not close:
    length1 = float(input("What is the length (m): "))
    wide1 = float(input("What is the wide (m): "))

    print(f"\nThe perimeter of the object is {rectangle(length1, wide1)} ")

    try_again = input("\nDo you want to try again? (Y/N)\n")
    if try_again.upper() == "Y":
        close = False
    else:
        close = True
