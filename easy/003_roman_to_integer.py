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