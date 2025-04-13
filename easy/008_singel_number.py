def singl_num(nums):
    d ={}
    for i in range(len(nums)):
        if nums[i] in d :
            d[nums[i]] = d[nums[i]]+1
        else :
            d[nums[i]] = 1
    return next((k for k , v in d.items() if v == 1),None)


arr = [4,1,2,1,2]
print(singl_num(arr)) # return the number that write one item