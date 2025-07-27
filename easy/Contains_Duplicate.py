

"""def containsDuplicate( nums):
    dic = {}

    for i in nums :
        if i in dic :
            dic[i] =  dic[i]+1
            return True
        else:
            dic[i] = 1

    return False"""

def containsDuplicate( nums):
    set_ = set()

    for i in nums:
        if i in set_:
            return True
        set_.add(i)
    return False

print(containsDuplicate([1,2,2,3]))