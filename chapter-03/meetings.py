def can_attend_meeting(intervals):

    def overlap(interval1, interval2):
        return (interval1[0] >= interval2[0] and interval1[0] < interval2[1] or interval2[0] >= interval1[0] and interval2[0] < interval1[1])


    for i in range(len(intervals)):
        for j in range(i +1 , len(intervals)):
            if overlap(intervals[i], intervals[j]):
                return False
        return True



print(can_attend_meeting(([0,30], [5,10], [5,20])))
print(can_attend_meeting(([7,10], [2,4])))


def can_attend_meeting_v2(intervals):
    stack = []

    sorted_interval = sorted(intervals)

    for interval in sorted_interval:

        if (len(stack)) == 0:
            stack.append(interval)

        elif(interval[0] > stack[-1][-1]):
            stack.append(interval)

        else:
            return False

    return True


print(can_attend_meeting_v2(([0,30], [5,10], [15,20])))
print(can_attend_meeting_v2(([7,10], [2,4])))



def can_attend_meeting_v3(intervals):
    intervals.sort()

    for i in range(len(intervals) -1):
        if(intervals[i][1] > intervals[i+1][0]):
            return False
    return True

print(can_attend_meeting_v3(([0,30], [5,10], [15,20])))
print(can_attend_meeting_v3(([7,10], [2,4])))
