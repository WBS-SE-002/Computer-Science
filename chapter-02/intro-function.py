# definition
def greet_person():
    print("Hello Person!")


# calling a function
# greet_person()
# greet_person()
# greet_person()
# greet_person()
# greet_person()


def greet_person2(person):
    print(f"Hello {person}")


print(greet_person2("steve"))

# greet_person2("karl")
# greet_person2("hannah", "jane")


def simple_add_numbers(a, b):
    print(a)
    print(b)
    return a + b


result = simple_add_numbers(2, 3)
print(result)

# a = int(input("First number: "))
# b = int(input("Second Number: "))

# simple_add_numbers(a, b)


def add_user_input():
    a = int(input("First number: "))
    b = int(input("Second Number: "))
    print(a+b)


# add_user_input()


def greetPerson3(name="guest", greeting="hi"):
    print(f"{greeting} {name}")


greetPerson3("karl", "hello")

greetPerson3(greeting="salut", name="karla")

greetPerson3()

greetPerson3(name="jane")
greetPerson3(greeting="salut")


def just_positional_argument(a, b, c, /):
    print((a, b, c))


# just_positional_argument(a=1, b=2, c=2)


def just_keyword_arguments(*, a, b, c):
    print((a, b, c))


just_keyword_arguments(a=1, c=2, b=3)


def combined_args(a, b, c, /, *, d): {
    print((a, b, c, d))
}


combined_args(1, 2, 3, d=5)


print("hello world", "salut", sep="*")
print("salut", end="-----")


def printNumbers(*numbers):
    print(type(numbers))
    for num in numbers:
        print(num)


printNumbers(1, 2, 3, 4, 5, 6, 7, 9)


printNumbers("1", "2", "hello", "world", "python")


def print_arguments(*args):
    for item in args:
        print(item)


print_arguments(1, 2, "3", 2)


def printNames(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print(kwargs[key])


printNames(personA="john", personB="jane", personC="karl")


def printDate():
    print("today is wednesday")


def printResult(result):
    print(f"The result is: {result}")
    printDate()


def add_numbers(a, b):
    result = a + b
    printResult(result)
    return a + b


# add_numbers(3, 4)


# error handling


def divide_10_by_number(number):
    try:
        result = 10 / number
    except TypeError:
        print("That's not a valid number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"The result is {result}")
    finally:
        print("I always run")


divide_10_by_number("3")
divide_10_by_number(0)
divide_10_by_number(2)


my_list = [1, 2, 3, 4]

try:
    my_list.index(10)
except ValueError:
    print("This value is not in the list")


def outer_function(fn, *args):
    print("I am the outer function and I will call the passed in function")
    fn(*args)
    print("Told you so")


outer_function(greet_person)

outer_function(simple_add_numbers, 2, 3)


outer_function(lambda: print("i am a lambda function"))

outer_function(lambda x: print(
    f"I am a lambda function, too. This is what I print: {x}"), 5)


def mulitply_by_n(mulitplier):
    # def multiply(number):
    #   return mulitplier * number
    #    return multiply
    return lambda number: mulitplier * number

    # def multiply(number):
    # return 3 * number


def multiply_by_threeB(number):
    return 3 * number


multiply_by_three = mulitply_by_n(3)
print(multiply_by_three)
multiply_by_five = mulitply_by_n(5)

print(multiply_by_three(4))

# return 3 * 4

print(multiply_by_five(10))


def output_multiple_value(a, b, c):
    return [a, b, c]
