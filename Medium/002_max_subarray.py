def maxSubArray(nums):
    if len(nums) == 1:
        sub_sum = nums[0]
        return sub_sum
    elif len(nums) == 0:
        return None
    else:
        # nums = [-2,1,-3,4,-1,2,1,-5,4]
        sub_sum = nums[0]
        sub_arr = [nums[0]]
        for i in range(1,len(nums)):
            




