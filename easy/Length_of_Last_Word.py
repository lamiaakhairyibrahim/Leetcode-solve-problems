


# s = "lamiaa khairy"
# d = s.split(" ")
# print(type(d))
def lengthOfLastWord(s):
    l = s.split()
    print(l)
    return len(l[-1])
print(lengthOfLastWord("lamiaa khairy "))