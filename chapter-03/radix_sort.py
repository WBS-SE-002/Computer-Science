def get_digit(number, d):
    """Return d-th digit of number, where d=0 is LSD."""
    return (number // 10**d) % 10

def counting_sort_by_digit(arr, d):
    """Stable counting sort of arr by digit d."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for value in arr:
        digit = get_digit(value, d)
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        digit = get_digit(arr[i], d)
        count[digit] -= 1
        new_index = count[digit]
        output[new_index] = arr[i]
    return output

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    k = 0
    while 10**k <= max_val:
        arr = counting_sort_by_digit(arr, k)
        k += 1
    return arr

my_array = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_array = radix_sort(my_array.copy())
print("Original Array:", my_array)
print("Sorted Array:", sorted_array)