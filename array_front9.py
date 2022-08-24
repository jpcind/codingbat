def array_front9(nums_list):
    if len(nums_list) <= 4:
        if 9 in nums_list:
            return True
        return False
    my_list = []
    for i in range(4):
        my_list.append(nums_list[i])
    if 9 in my_list:
        return True
    return False
