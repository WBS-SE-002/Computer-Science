def add(numbers):

    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + add(numbers[1:])


add([1, 2, 3, 4])


def add_numbers_loop(numbers):
    sum = 0
    for num in numbers:
        sum += num


"""
add([1,2,3,4]) -> 1 + add([2,3,4])
add([2,3,4]) -> 2 + add[3,4]
add([3,4]) -> 3 + add([4])
add([4]) -> 4

3 + 4
2 + 7
1 + 9
-> 10
"""


def reverse_string(string):
    if len(string) == 1:
        return string

    result = reverse_string(string[1:]) + string[0]
    print(result)
    return result


reverse_string("hello")


"""
reverse_string("hello") -> reverse_string("ello") + "h"
reverse_string("ello") -> reverse_string("llo") + "e"
reverse_string("llo") -> reverse_string("lo") + "l"
reverse_string("lo") -> reverse_string("o") + "l"
reverse_string("o") -> "o"

"o" + "l"
"ol" + "l"
"oll" + "e"
"olle" + "h"
-> "olleh"

"""


def factorial(n):
    pass


"""
5!
5*4*3*2*1
"""
