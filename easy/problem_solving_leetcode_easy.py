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


# problem(2) /////////////////// Palindrome Number ////////////////
def isPalindrome(self, x: int) -> bool:
        n = str(x)[::-1]
        if n == str(x):
              return True
        else:
               return False
        
# problem(3) ///////////////////// Roman to Integer //////////////
# //// way 1 ////
def romanToInt(self, s: str) -> int:
        d = { 
           'I' :  1,
           'V' :  5,
           'X' :  10,
           'L' :  50,
           'C' :  100,
           'D' :  500,
           'M' :  1000
         }
        number = 0
        old = 0
        for char in reversed(s):
            new = d[char]
            if new < old:
               number -= new
            else:
                number += new
            old = new

        return number
# //// way 2 ////
def romanToInt(self, s: str) -> int:
        d = { 
           'I' :  1,
           'V' :  5,
           'X' :  10,
           'L' :  50,
           'C' :  100,
           'D' :  500,
           'M' :  1000
         }
        number = 0
        for i in range(len(s)):
                if i < (len(s)-1) and d[s[i]] < d[s[i+1]]:
                    number = number - d[s[i]]
                else:
                      number += d[s[i]]
        return number
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
#problem(5) ////////////////  Valid Parentheses ////////////////////////////////
"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""
#####
"""def isValid( s: str):
    d = { '(' : ')',
          '[' : ']',
          '{' : '}'
        }
    if not s :
         return False
    for i,ch in enumerate(s):
        print("i = ",i)
        if ch in d :
            index_char = s.find(d[ch])
            print("index = " , index_char)
            if index_char == -1 :
                return False          
    return True

    
#print(isValid("([)]"))
print(isValid("([])"))"""
def isValid(s):
    # Initialize a stack to be used in the algorithm.
    stack = []
    
    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}
    
    # For every character in the input string
    for char in s:
        
        # If the character is an closing bracket
        if char in mapping:
            
            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            #top_element = stack.pop() if stack else '#'
            if stack:
                 top_element = stack.pop()
                 """print("top_element : ",top_element)
                 print("stak : " , stack)"""
            else:
                 top_element = '#'
                 
            
            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)
    
    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack
#print(isValid("((()"))
# problem(6) ///////////////////////marge two sorted list /////////////////////////
def two_list(nums1 , nums2):
    nums3 = []
    short = min(len(nums1 ), len(nums2)) 
    longest = max(len(nums1),len(nums2))
    for i in range(longest):
        if i < short :
            nums3.append(min(nums1[i] , nums2[i]))
            nums3.append(max(nums1[i] , nums2[i]))
        elif len(nums1) > len(nums2) :
             nums3.append(nums1[i])
        else:
             nums3.append(nums2[i])
    return nums3
#print(two_list([] , [0]))
"""class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next"""
#problem(7) /////////////////////////////
