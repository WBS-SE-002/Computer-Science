my_tuple = (1, 2, 3, 4)

print(my_tuple[2:])


print("1" in my_tuple)

temp_list = list(my_tuple)

print(type(temp_list))

back_to_tuple = tuple(temp_list)
print(type(back_to_tuple))


nested_tuple = (1, 2, ["a", "b"], 3, 5)

nested_tuple[2][0] = "z"
print(nested_tuple)

# nested_list = [1,2,("a", "b"), 3]

# nested_list[2][0] = "z"

# print(nested_list)
my_animals = ("orca", "hammerhead shark", "showbill", "lion", "ocean sunfish")

my_favorite_animal = my_animals[0]
my_second_favorite_animal = my_animals[1]
my_sub_list = my_animals[1:4]
print(my_favorite_animal)
print(my_second_favorite_animal)

(x, *y, z) = my_animals

print("x", x)
print("y", y)
print("z", z)

print(type(z))

my_first = (1, 2, 3, 1)
my_second = (4, 5, 6)

combined = my_first + my_second
print(combined)

multiplied = my_first * 3 + my_second * 2
print(multiplied)

print(my_first.count(10))

print(my_first.index(1))
