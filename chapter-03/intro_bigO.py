numbers = [1, 2, 3]


# O(1) - contant time and space
def printNumbersA(nums):
    print(nums[-1])


printNumbersA(numbers)

# O(n)


def printNumbersB(nums):
    for num in nums:
        if num == 2:
            break
        print(num)
        print(num)


printNumbersB(numbers)

# O(n^2)


def printNumbersC(nums):
    count = 0
    for num in nums:
        for num in nums:
            print(num)
            count += 1
    print(count)


# printNumbersC(numbers)


# O(n^3)
def printNumbersD(nums):
    count = 0
    for num in nums:
        for num in nums:
            for num in nums:
                print(num)
                count += 1
    print(count)


printNumbersD(numbers)

["a", "b", "c", "d", "e", "f", "g"]


sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
               15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


searchItem = 5


def sort_alg(num):
    intermediate_list = []
    for n in num:
        intermediate_list.append(n)


""" 2x^2 + 2n + 5"""
