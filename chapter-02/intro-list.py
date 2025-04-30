# create and name a list
fruits = ["apple", "banana", "cherry"]

print(fruits)

# access an item
print(fruits[2])

# change
# add an item

fruits.append("cucumber")
print(fruits)

fruits[1] = "blueberry"
print(fruits)

# remove
fruits.remove("cherry")
print(fruits)


# duplicates
fruits.append("cucumber")
print(fruits)

print(fruits[2:])

print("apple" in fruits)

fruits.insert(2, "peach")
print(fruits)

another_list = ["car", "bus", "tram"]

fruits.extend(another_list)
print(fruits)


fruit = fruits.pop(1)
print(fruits)
print(fruit)

# fruits.clear()
print(fruits)

my_numbers = [1, 2, 3, 4, 5]

for num in my_numbers:
    print(num)
    for innerNum in my_numbers:
        print(innerNum)


# swap elements

alphabet = ["a", "b", "c", "d", "e"]


alphabet[1], alphabet[3] = alphabet[3], alphabet[1]

print(alphabet)


# list comprehension

new_list = [num for num in my_numbers if num > 3]


new_list2 = [char + char for char in alphabet]
print(new_list2)

# [exression, loop (iteration), condition]
print(new_list)
print(my_numbers)


letters = ["A", "B", "C"]

pairs = [x + y for x in letters for y in letters if x != y]
print(pairs)


random_numbers = [5, 2, 3, 1, 9]

# random_numbers.sort()
print(random_numbers)

new_numbers = [x for x in sorted(random_numbers) if x % 2 != 0 and x > 2]
print(new_numbers)


random_alphabet = ["b", "d", "f", "g", "G", "A"]
random_alphabet.sort(reverse=True)
print(sorted(random_alphabet, reverse=True))
# print(random_alphabet)


my_best_list = ["karl", "hannah", "john"]

# my_best_listB = my_best_list
# my_best_list.append("jane")
# print(my_best_list)
# print(my_best_listB)

my_best_listC = my_best_list.copy()
my_best_listC = my_best_list[:]

c_list = [1, 2, 3]
d_list = [4, 5, 6]

c_list.append(d_list)
print(c_list)

print(c_list[3][1])


vending_machine = [{"name": "a", "price": 20.50}, {
    "name": "b", "price": 2.50}, {"name": "c", "price": 17.50}]


def sortingPrices(dict):
    return dict["price"]


vending_machine.sort(key=lambda x: x["price"])

print(vending_machine)

my_list = ["orca", "humpback whale",
           "Hammerhead shark", "ocean sunfish", "stringray"]


new_list = [animal[0] + animal[1:]
            for animal in my_list if animal[0].islower()]
print(new_list)
