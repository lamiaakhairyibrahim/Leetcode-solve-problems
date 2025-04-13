# problem(1) /////////////////// two sum ///////////////////////////
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""
from typing import List
# //// way (1) ////
def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n = i+1
            for  n in range(n,len(nums)):
                if target == nums[i]+nums[n]:
                    return [i,n]
# //// way (2) ////
def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0 , len(nums)):
            y = 0
            y = target - nums[i]
            if y in d :
                  return [d[y] , i ]
            else:
                d[nums[i]] = i
# //// way (3) /////
def twoSum(nums , target ):
    for i in range(len(nums)):
        num = target - nums[i]
        for j in range(i+1 , len(nums)):
            if nums[j] == num :
                return [i , j]
nums = [3,2,4]
target = 6
print(twoSum(nums , target ))