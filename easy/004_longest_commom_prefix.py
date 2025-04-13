# problem (4) ///////////////////////////// Longest Common Prefix /////////////////////////////
from typing import List
def longestCommonPrefix( strs: List[str]):
    short_str = min(strs, key=len)  # Find the shortest string in the list  
    for i, char in enumerate(short_str):
        for other in strs :
            # check all strs in list of strs 
            #strs = ["flower","flow","flight"]
            #short_strs = "flow"
            #if i = 0 
            #other[0] = "f" in "flower"
            #other[0] = "f" in "flow"
            #other[0] = "f" in "flight"
            if other[i] != char :
                return short_str[:i]
    return short_str

print(longestCommonPrefix(["abcgfhf","fll","flight"]))