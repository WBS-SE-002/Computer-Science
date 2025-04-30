my_list = [2,5,4,8,9,10,7,12]



def linear_search(arr, target):
    # for num in arr:
    #     if num == target:
    #         return num

    # for i in range(len(arr)):
    #     if arr[i] == target:
    #         return i

    for i, num in enumerate(arr):
        if num == target:
            # return [i, num]
            return {"index": i, "value": num}
    return -1


print(linear_search(my_list, 9))