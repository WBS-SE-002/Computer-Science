def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

        return arr


my_list = [1, 2, 3, 4, 5]


[18, 18, 18, 18, 17, 17, 16, 12, 12, 12]
# comparing n -> n-1 items n*n -> n^2
# swapping n - > n-1 items

bubble_sort(my_list)

print(my_list)
