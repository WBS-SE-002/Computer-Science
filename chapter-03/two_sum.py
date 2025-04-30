def two_sum(num_list, target):
    length = len(num_list)

    for i in range(length):
        for j in range(i+1, length):
            if num_list[i] + num_list[j] == target:
                return [i, j]
    
print(two_sum([3,2,4], 6))
print(two_sum([2,7,11,15], 9))
print(two_sum([3,3], 6))



def two_sum_v2(num_list,target):
    seen = {}

    for i, num in enumerate(num_list):
        complement = target-num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i


print(two_sum_v2([3,2,4], 6))


my_dictionary = {}

my_dictionary["name"] = "karl"