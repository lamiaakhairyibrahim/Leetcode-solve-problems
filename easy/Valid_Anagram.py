
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    else:
        dic = {}
        