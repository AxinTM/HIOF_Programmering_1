animal = {
    "species": "HoneyBadger",
    "name": "Nils",
    "sex": "Male"
}

print(f"The animals name is {animal['name']}")

animal["sex"] = "Notoriously difficult to determine for honey badgers"
print(f"\n{animal['sex']}")

animal["age"] = 35

print(f"\n{animal}")
