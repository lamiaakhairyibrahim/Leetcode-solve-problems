# problem(2) /////////////////// Palindrome Number ////////////////
def isPalindrome(self, x: int) -> bool:
        n = str(x)[::-1]
        if n == str(x):
              return True
        else:
               return False