def permute(nums):
    permute_list=[]
    for i in range(len(nums)):
        print(i)
        permute_list.append(nums[i])
        for j in range(len(nums)):
            if i != j:
                permute_list.append(nums[j])

    return print(permute_list)

permute([1,2,3])