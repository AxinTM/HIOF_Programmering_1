from math import log


def dog_to_human_year(dog_age):
    # 16 * log(<dog_age> + 31
    human_equivalent_age = 16 * log(dog_age) + 31
    return int(human_equivalent_age)


print(dog_to_human_year(10))
