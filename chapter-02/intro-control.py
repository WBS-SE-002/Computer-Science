print("a")
name = "karl"
print("b")
print("c")

name = "hannah"

print(name)

a = 20
b = 15

print((a <= b) or (b >= a))

print(not (5 == 5))


if b != 15:
    print("15")
elif a != 20:
    print("20")
else:
    print("default")


result = "true" if 2 != 2 else "false"
print(result)


# while loop

count = 0

while count < 5:
    count += 1
    if count == 3:
        continue
    else:
        print("not continue")
    print(count)
else:
    print("something else")


fruits = ["apple", "banana", "cherry"]
vehicles = ["car", "bike", "ship"]


for fruit in fruits:
    print(fruit)
    for vehicle in vehicles:
        print(vehicle)


for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("default")


my_dict = {
    "firstName": "Karl",
    "lastName": "Karlsen"
}


vending_machine = {
    "chocolate": {
        "amount": 10,
        "price": 5
    }
}


vending_machine2 = [{"name": "chocolate", "amount": 10, "price": 5}, {
    "name": "banana", "amount": 10, "price": 2}]


vending_machine3 = [{"chocolate": {"amount": 10, "price": 5}}, {"banana"}]

user_input = 3

if vending_machine["chocolate"]["price"] > user_input:
    print("not enough money")


for x in my_dict:
    print(x)


day = (5, 2)


# match day:
#   case(5, 1):
#      print("monday")
# case(5, 2):
#    print("tuesday")
#  case(5, 3):
#  print("wednesday")
# case _:
#    print("something else")


my_list = [5, 3, 2, 1, 6]


my_list[0], my_list[1] = my_list[1], my_list[0]

print(my_list)


for i in range(10):
    pass
