# print("Hello")

# Skjelett
import random


def function():
    # logikk
    return

function()

def print_hello():
    print("----------------")
    print("     Hello!     ")
    print("----------------")
    return

print("Først")

print_hello()

print("Sist")
'''
# return
def give_random_number():
    random_number = random.randrange(1, 11)
    return random_number

number = give_random_number()
print(f"\n{number}")
'''

#range_start = 5
#range_stop = 10

# parametere
def give_random_number(range_start, range_stop):
    random_number = random.randrange(range_start, range_stop)
    return random_number

# range = 1 - 100
random_number_variable = give_random_number(1, 101)
print(random_number_variable)

# range = 50 - 55
