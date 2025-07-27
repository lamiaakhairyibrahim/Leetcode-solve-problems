

"""s = 'lAmiaa234'
s1 = []
for i in range(len(s)):
    if s[i].isalpha():
        s1.append(s[i])

print(s1)
print(s.isalpha())
print(s.capitalize())
print(s.lower())
print(s.upper())"""
#for i in s :
#   if i.isalpha():
#        print(i)
#    else:
#        print("no")

"""def isPalindrome(s):
        if len(s) == 1:
            return True
        s = s.lower()
        s1 = []
        for i in range(len(s)):
            if s[i].isalnum():
                s1.append(s[i])
        left , right = 0 , len(s1)-1
        while left < right:
            if s1[left] != s1[right]:
                return False
            left = left + 1
            right = right -1 
        return True"""
def isPalindrome(s):
    s = s.lower()
    left, right = 0, len(s) - 1

    while left < right:
        # تجاهل الحروف غير الأبجدية الرقمية من اليسار
        while left < right and not s[left].isalnum():
            left += 1
        # تجاهل الحروف غير الأبجدية الرقمية من اليمين
        while left < right and not s[right].isalnum():
            right -= 1
        # المقارنة
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
print(isPalindrome(".p"))

    