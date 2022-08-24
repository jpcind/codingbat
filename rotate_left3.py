def rotate_left3(nums):
    if len(nums) != 3:
        return None
    nums.append(nums.pop(0))
    return nums

def main():
    print(rotate_left3([1, 2, 3]))

main()
