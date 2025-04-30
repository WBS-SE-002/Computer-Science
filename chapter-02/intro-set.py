my_set = {1, 2, 3, 4, 5}

my_list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]

my_second_set = set(my_list)

print(my_second_set)

print(set("hello"))


for item in my_set:
    print(item)


my_set.add(2)
print(my_set)

my_set.update({10, 11, 12, 13})

new_set = my_set.union({20, 30, 40, 50})
# removed_item = my_set.pop()
# print(removed_item)
# my_set.clear()
print(my_set)
print(new_set)

# my_set.remove(3)
# print(my_set)

# my_set.remove(9)


my_set.discard(6)
# print(my_set)


# print(5 not in my_set)

first_set = {1, 2, 3, 4, 5, 6}
second_set = {5, 6, 7, 8, 9}

print(first_set.intersection(second_set))

print(first_set.difference(second_set))
print(second_set.difference(first_set))

print(first_set.symmetric_difference(second_set))


third_set = {1, 2, 3, 4, 5, 6, 7}
fourth_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(third_set.issubset(fourth_set))
print(fourth_set.issuperset(third_set))

print(third_set < fourth_set)
print(fourth_set > third_set)


print({1, 2, 3, 4}.isdisjoint({5, 6, 7, 8}))


set_a = {"a", "b", "c", "d"}
set_b = {"c", "d", "e", "f"}

# set_a.difference_update(set_b)
print(set_a.intersection_update(set_b))
print("---")
print(set_a.intersection(set_b))
print(set_a)


def foo():
    set_a.add("orca")


foo()

result = foo()

print(result)
print(set_a)


def add(a, b):
    return a + b


add(10, 5)
