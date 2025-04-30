persons = {
    "firstName": "Karl",
    "lastName": "Karlsen",
    "city": "Berlin",
    "friends": ["Hannah", "John", "Jane"],
    "characteristic": {
            "hair": "blond",
            "height": 1.70
    }}


print(persons.get("characteristic", {}).get("height", 1.00))


# print(persons["personA"]["friends"])

# print(persons["personA"]["friends"][2])

# print(persons["personA"]["characteristic"]["height"])

# persons["personA"]["characteristic"]["height"] = 2.00

# print(persons["personA"]["characteristic"]["height"])

# del persons["personB"]

# print(persons)

# person_a = persons.get("personC", "nothing here").get()
# print(person_a)


keys = list(persons.keys())


# for key in keys:
#   print(key)
#  print(persons[key])

# print(persons)


values = persons.values()
# print(values)

items = list(persons.items())

# for x, y in items:
#   print(y)

# print(items)


# print("city" in persons)


persons.update({"favoriteFruit": "cherry", "pet": "dog"})
# print(persons)


deleted_item = persons.pop("favoriteFruit")
# print(deleted_item)

# print(persons)

last_item = persons.popitem()
# print(last_item)

persons.clear()

# print(persons)


my_bike = {
    "size": "m",
    "color": "purple",
    "brand": "trek",
    "owner": {
        "firstName": "Karl",
        "lastName": "Karlsen"
    }
}

print(my_bike["color"])
print(my_bike.get("color", "red"))

# print(my_bike["house"])

print(my_bike["owner"]["firstName"])
print(my_bike.get("owner", {}).get("firstName"))

my_second_bike = my_bike.copy()


print(my_second_bike["owner"] is my_bike["owner"])
my_bike["owner"]["firstName"] = "Carl"

print(my_bike)
print(my_second_bike)

del my_bike["owner"]


if my_bike.get("owner") != None:
    print(my_bike["owner"])
else:
    print("not found")


if "owner" in my_bike:
    print(my_bike["owner"])
else:
    print("not found")
