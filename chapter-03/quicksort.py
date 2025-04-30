def quicksort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index -1)
        quicksort(arr, pivot_index +1, right)
    return arr



def partition(arr, left, right):
    pivot_value = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i +1


my_list = [10,7,8,9,1,5]

quicksort(my_list, 0, len(my_list)-1)

print(my_list)
