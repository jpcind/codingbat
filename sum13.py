def sum13(nums):
    my_sum = 0
    flag = False
    for i in nums:
        if i == 13:
            flag = True
            continue
        if flag:
            flag = False
            continue
        my_sum += i
    return my_sum





def main():
    my_list = [1, 2, 13, 2, 1, 13]
    my_list2 = [13, 1, 2, 13, 2, 1, 13]
    print(sum13(my_list2))

main()
