
## 10+1 = 11
## 11+1 = 12
## 12+1 = 13
## 19 +1 = 20

def PlusOne(nums):
    if nums[-1] < 9:
        nums[-1] = nums[-1] + 1
        return nums
    else :
        nums_1 = ''.join(str(i) for i in nums)
        print("nums_1 :" , nums_1)
        nums_2 = int(nums_1) + 1
        nums_3 = str(nums_2)
        return [int(i) for i in nums_3]
        
print(PlusOne([9,9]))