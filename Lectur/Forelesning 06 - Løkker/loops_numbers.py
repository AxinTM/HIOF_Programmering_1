print("\nPrint number from 0 to 10:")
for number in range(11):
    print(number)

print("\nPrint number from 0 to 9:")
for number in range(1, 10,):
    print(number)

print("\nPrint number from 1000 to 9001:")
for number in range(1000, 9001,):
    print(number)

print("\nPrint number from 1000 to 9001, with interval/step of 1000:")
numbers = []
for number in range(1001, 9002, 1000):
    print(number)
    numbers.append(number)

print("")
print(numbers)

print(f"\nMinimum: {min(numbers)}")
print(f"\nMaximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

numbers = list(range(2, 101, 2))
print(numbers)
