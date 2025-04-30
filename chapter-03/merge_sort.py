def merge_sort(nums):
    length = len(nums)

    if length < 2:
        return nums

    mid = length // 2
    left = nums[:mid]
    right = nums[mid:]

    sortedLeft = merge_sort(left)
    sortedRight = merge_sort(right)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    results = []

    while len(left) and len(right):
        if left[0] <= right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))

    if not results:
        return left + right
    if left:
        results.extend(left)
    if right:
        results.extend(right)
    return results

        

print(merge_sort([38,27,43,3,9,82, 10]))