

"""def reverseString(s) :
    l = len(s) // 2
    print("s : " , s )
    for i in range(l):
        temp = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = temp 

    return s"""

def reverseString(s):
    left , right = 0 , len(s)-1
    while left < right :
        s[left] , s[right] = s[right] , s[left]
        left = left +1 
        right = right -1 

    return s

print("s2: " ,reverseString(["l" , "a" , "m"]))