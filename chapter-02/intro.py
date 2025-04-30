import random
#print("Hello, World!")




#for i in range(5):
    #print("hello")

#print("world")

my_age = 25

def hello(a,b):
    print("inside",my_age)
    for i in range(2,5, 2):
       print(i)
    return a +b

#hello(2,3);

#print("outside",my_age)

name = "Alice"
# this looks really cool!
#print(name)

#print("Hello, my name is", name)


#print("salut")


age = "20"
Age = 20

#print(type(int(age)))

#print("Hello 'World'!")
#print('Hello, "World"!')


#print("My age is " + str(Age))


#print(int("hello"))

my_number = 20
my_number = "hello"
#print(my_number)


my_list = [1,2,3]

my_tuple = (1,2,3)



my_dict= {
    "name": "Alice",
    "age": 30,
    "isMarried": True,
}

#print(my_dict)

my_set = {1,2,3,4,5,2,3,4,5}

#print(my_set)

def my_function():
    print("hello")

#print(my_function())


clothes = {
    "jeans": {
        "amount": 1,
        "price": 20.50
    },
    "hat": {
        "amount": 20,
        "price": 1.50
    }
}


my_clothes = [{"name": "jeans", "amount": "20", "price": 20.50}, {}]




age = 20
price = 20.50

print(random.randint(1,10))

print(random.random())

print(random.uniform(5,10))

print(random.randint(1,6))


print("hello")
print('world')
print("""chapter 1 
hello""")

#print("hello"[5])

word = "abcdefgh"
for char in word:
    print(char)


print(word[::2])

print(len(word))

print("ab" not in word)

print("    hello world ".strip())

print(word.replace("ab", "zc"))

print(word.split("d"))

first_name = "Karl"

print(f"Hello, I am {first_name}")

print("Hello hello \"salut\" salut  first_name salut")

print(word.count("d"))



if 1!=1 or 2 != 2 and 3==3:
    print("true")
else: 
    print("false")



print({name: "karl"} is {name: "karl"})