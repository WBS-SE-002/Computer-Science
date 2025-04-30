def counting_sort(arr, max_val):
    count = [0] * (max_val +1)
    for x in arr:
        count[x] += 1

    for i in range(1, max_val+1):
        count[i] += count[i-1]


    n = len(arr) 
    result = [0] * n


    for i in range(n-1, -1, -1):
        x = arr[i]
        count[x] -= 1
        new_index = count[x]
        result[new_index] = x

    return result



# print(counting_sort([4,2,2,8,3,3,1], 8))



def counting_sort_dictionaries(arr, max_val, min_val, key):
    count = [0] * (max_val - min_val +1)
    for x in arr:
        idx = x[key]
        count[idx - min_val] += 1

    for i in range(1, max_val - min_val+1):
        count[i] += count[i-1]
    n = len(arr)
    result = [0] * n

    for i in range(n-1, -1, -1):
        x = arr[i]
        idx = x[key] - min_val
        count[idx] -= 1
        new_index = count[idx]
        result[new_index] = x


    return result




print(counting_sort_dictionaries(
    [{"age": 20, "name": "karl"}, {"age": 22, "name": "hannah"}, {"age": 18, "name": "jenny"}, {"age": 22, "name": "jane"}, {"age": 18, "name": "karla"}], max_val=22, min_val=18, key="age"))
