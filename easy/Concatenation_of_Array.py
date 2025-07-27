

def getConcatenation( nums):
    ans = []
    for i in nums:
        ans.append(i)
    return ans+nums

print(getConcatenation([1,3,2,1]))
