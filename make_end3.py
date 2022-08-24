def max_end3(nums):
    if len(nums) != 3:
        return None
    greater = max(nums[0],nums[-1])
    i = 0
    while i < len(nums):
        nums[i] = greater
        i += 1
    return nums
