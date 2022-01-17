print("=============Odd numbers from for-loop=============")
print("\nPrinting all odd number from 9 to 101")
for number in range(9, 102, 2):
    print(number)

# definere start tallet og lage en tom liste for odde tall
start_number = 9
odd_number = []
# printer ut som while loop
print("\n=============Odd numbers from while-loop=============")
while start_number <= 101:
    odd_number.append(start_number)
    print(start_number)
    # legger til 2 på start tallet, og det som kommer ut i listen
    start_number += 2
# printer ut som for loop.
for x in odd_number:
    print(f"\n{x} is an odd number!")
