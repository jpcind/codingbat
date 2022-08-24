def array123(nums):
    if len(nums) == 0:
        return False
    try:
        for i in range(len(nums)):
            if nums[i] == 1:
                if nums[i+1] == 2:
                    if nums[i+2] == 3:
                        return True
    except IndexError:
        return False

def main():
    print(array123([1,1,2,3,1]))
    print(array123([1,1,2,4,1]))
    print(array123([1,1,2,1,2,3]))

main()
