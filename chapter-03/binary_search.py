my_list = [1,2,3,4,6,7,10,12,33,44,55,99]


def binary_search(arr, target):
    left = 0
    right = len(arr)-1


    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid +1
        else:
            right = mid -1

    return -1



print(binary_search(my_list, 2))