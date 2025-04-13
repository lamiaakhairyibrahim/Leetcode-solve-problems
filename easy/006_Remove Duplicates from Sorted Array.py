#  -------  problem 6 -----
#--------------------------
def removeDuplicates(nums):
    k = 1
    new_num = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i] == new_num[-1]:
                continue
        else:
            new_num.append(nums[i])
            k += 1
    return k , new_num
        
#print(F"the list that content only unique number is : {new_num} , number of element is : {k}")
print(removeDuplicates([12,12,14,14,14,17,18]))

# --- way 2 ----------------------------------------
def removeDuplicates(nums):
                k = 1
                for i in range(1, len(nums)):
                    if nums[i] != nums[i- 1]:
                        nums[k] = nums[i]
                        k += 1
                return k
#-----------------------------------------------

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
def removeDuplicates(arr):
    k = 0
    l = []
    for i in range(len(arr)):
            if len(l) == 0:
                  l.append(arr[i])
            elif l[len(l)-1] == arr[i]:
                  k+=1
            else:
                  l.append(arr[i])
    return len(l) ,l

nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums) 
print(removeDuplicates(nums) )
