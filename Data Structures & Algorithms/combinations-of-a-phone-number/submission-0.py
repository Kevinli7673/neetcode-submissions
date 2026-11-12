"""
Given that each number is mapped to 3-4 numbers, return the combinations of alphabets that can be represented with the given numbers 
First we're gonna have a hashmap that maps the alphabets to their digits, then we have a for loop iterating through each hashmap
and a inner loop that loops through each value in each key
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []

        digitsmap = {"2": "abc",
                  "3": "def",
                  "4": "ghi",
                  "5": "jkl",
                  "6": "mno",
                  "7": "pqrs",
                  "8": "tuv",
                  "9": "wxyz"}

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for digit in digitsmap[digits[i]]:
                backtrack(i+1, curStr + digit)
        
        if digits:
            backtrack(0, "")
        return res


