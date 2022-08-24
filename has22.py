def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

def main():
    mylist2 = [1, 2, 2]
    mylist3 = [1, 2, 1, 2]
    mylist = [2, 1, 2]

    mylist4 = [2, 1, 2, 2, 1, 2]
    mylist5 = [1, 2, 2, 1, 2]
    mylist6 = [2, 2, 1, 2, 2]

    print(has22(mylist6))



main()
