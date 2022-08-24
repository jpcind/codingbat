def sum67(nums):
    flag = False
    my_sum = 0
    if 6 not in nums:
        return sum(nums)
    for i in nums:
        if i == 6:
            flag = True
            continue
        if i == 7:
            if flag:
                flag = False
                continue
        if not flag:
            my_sum = my_sum + i
    return my_sum


